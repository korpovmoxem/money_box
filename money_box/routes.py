from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user

from money_box import app, db
from money_box.tools import UserAuth, DayGoals, DayInstances, create_day_goals, fill_days_db, fill_day_instances\
    , get_day_instances, get_day_goals, update_day_instance, change_total_goal, update_current_sum, write_log,\
    clear_logs, get_logs


@app.route('/')
def home_page():
    return render_template('home_page.html', counter=UserAuth.query.count())


@app.route('/info')
def info_page():
    return render_template('info_page.html', counter=UserAuth.query.count())


@app.route('/registration', methods=['GET', 'POST'])
def registration_page():
    email = request.form.get('email')
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Необходимо заполнить все поля')
        elif '@' not in email or '.' not in email:
            flash('Некорректный email')
        elif password != password2 or password == '' or password2 == '':
            flash('Пароли не совпадают')
        elif len(login) < 5:
            flash('Длина логина должна быть не меньше 5 символов')
        elif len(password) < 6:
            flash('Длина пароля должна быть не меньше 6 символов')
            return render_template('registration_page.html', counter=UserAuth.query.count())
        elif UserAuth.query.filter_by(email=email).first():
            flash('Пользователь с таким email уже существует')
        elif UserAuth.query.filter_by(login=login).first():
            flash('Пользователь с таким логином уже существует')
        else:
            if len(password) < 6:
                flash('Длина пароля должна быть не меньше 6 символов')

            hash_password = generate_password_hash(password)
            new_user = UserAuth(login=login, email=email, password=hash_password)
            db.session.add(new_user)
            db.session.commit()
            logout_user()

            return redirect(url_for('login_page'))
        return render_template('registration_page.html', counter=UserAuth.query.count())
    else:
        return render_template('registration_page.html', counter=UserAuth.query.count())


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('money_box'))
    login_email = request.form.get('login')
    password = request.form.get('password')
    reset_password_button = request.form.get('reset-password-button')
    reset_password_email = request.form.get('reset-password-email')

    if request.method == 'POST':
        if login_email and password:
             user = UserAuth.query.filter_by(login=login_email).first()
             if user and check_password_hash(user.password, password):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(url_for('money_box'))
             else:
                user = UserAuth.query.filter_by(email=login_email).first()
                if user and check_password_hash(user.password, password):
                    login_user(user)
                    next_page = request.args.get('next')
                    return redirect(url_for('money_box'))
                else:
                    flash('Логин/email или пароль неверны')
        # Восстановление пароля
        elif reset_password_button:
            validate_reset_password_email = UserAuth.query.filter_by(email=reset_password_email).first()
            if validate_reset_password_email:
                pass
        else:
            flash('Необходимо заполнить все поля')
    return render_template('login_page.html', counter=UserAuth.query.count())


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))


@app.route('/money_box', methods=['GET', 'POST'])
@login_required
def money_box():
    current_user_id = current_user.get_id()
    user = UserAuth.query.filter_by(id=current_user_id).first()
    goal_target = request.form.get('goal_target')
    new_goal_target = request.form.get('new_goal_target')

    try:
        # Регистрация нажатия кнопки
        if request.method == 'POST':
            buttons_list = []
            for i in range(1, 101):
                day_value = request.form.get(f"day_{i}_button")
                user_sum = DayGoals.query.filter_by(login=user.login).first()
                buttons_list.append(day_value)
                if day_value:
                    write_log(user.login, day_value)
            update_current_sum(user.login)
            update_day_instance(user.login, buttons_list)


    except:
        pass
    # Создание цели для нового пользователя
    if goal_target:
        if not goal_target.isdigit():
            flash('Необходимо ввести число')
            return render_template('money_box.html',
                            display=True, counter=UserAuth.query.count())
        elif int(goal_target) < 10000:
            flash('Число должно быть больше или равно 10000')
            return render_template('money_box.html',
                                   display=True, counter=UserAuth.query.count())
        day_goals = create_day_goals(goal_target)
        fill_days_db(user.login, day_goals, goal_target)
        fill_day_instances(user.login)

    # Изменение цели
    elif new_goal_target:
        change_total_goal(new_goal_target, user.login)
        day_goals = create_day_goals(new_goal_target)
        fill_days_db(user.login, day_goals, new_goal_target)
        fill_day_instances(user.login)
        current_goal = new_goal_target
        clear_logs(user.login)

    if not DayGoals.query.filter_by(login=user.login).first():
        return render_template('money_box.html',
                               display=True, counter=UserAuth.query.count())

    day_instances = get_day_instances(user.login)
    day_goals = get_day_goals(user.login)
    user_logs = get_logs(user.login)
    try:
        current_sum = DayGoals.query.filter_by(login=user.login).first().current_sum
        total_goal = DayGoals.query.filter_by(login=user.login).first().total_goal
    except AttributeError:
        current_sum = 1
        total_goal = 10
    current_goal = DayGoals.query.filter_by(login=user.login).first().total_goal
    return render_template('money_box.html',
                           display=False, current_sum=current_sum, total_goal=total_goal, progress_percent=current_sum / total_goal * 100,
                           current_goal=current_goal, user_login=user.login, user_logs=user_logs, counter=UserAuth.query.count(),
                           day_1_instance=day_instances[0], day_2_instance=day_instances[1], day_3_instance=day_instances[2],
                           day_4_instance=day_instances[3], day_5_instance=day_instances[4], day_6_instance=day_instances[5],
                           day_7_instance=day_instances[6], day_8_instance=day_instances[7], day_9_instance=day_instances[8],
                           day_10_instance=day_instances[9], day_11_instance=day_instances[10], day_12_instance=day_instances[11],
                           day_13_instance=day_instances[12], day_14_instance=day_instances[13], day_15_instance=day_instances[14],
                           day_16_instance=day_instances[15], day_17_instance=day_instances[16], day_18_instance=day_instances[17],
                           day_19_instance=day_instances[18], day_20_instance=day_instances[19], day_21_instance=day_instances[20],
                           day_22_instance=day_instances[21], day_23_instance=day_instances[22], day_24_instance=day_instances[23],
                           day_25_instance=day_instances[24], day_26_instance=day_instances[25], day_27_instance=day_instances[26],
                           day_28_instance=day_instances[27], day_29_instance=day_instances[28], day_30_instance=day_instances[29],
                           day_31_instance=day_instances[30], day_32_instance=day_instances[31], day_33_instance=day_instances[32],
                           day_34_instance=day_instances[33], day_35_instance=day_instances[34], day_36_instance=day_instances[35],
                           day_37_instance=day_instances[36], day_38_instance=day_instances[37], day_39_instance=day_instances[38],
                           day_40_instance=day_instances[39], day_41_instance=day_instances[40], day_42_instance=day_instances[41],
                           day_43_instance=day_instances[42], day_44_instance=day_instances[43], day_45_instance=day_instances[44],
                           day_46_instance=day_instances[45], day_47_instance=day_instances[46], day_48_instance=day_instances[47],
                           day_49_instance=day_instances[48], day_50_instance=day_instances[49], day_51_instance=day_instances[50],
                           day_52_instance=day_instances[51], day_53_instance=day_instances[52], day_54_instance=day_instances[53],
                           day_55_instance=day_instances[54], day_56_instance=day_instances[55], day_57_instance=day_instances[56],
                           day_58_instance=day_instances[57], day_59_instance=day_instances[58], day_60_instance=day_instances[59],
                           day_61_instance=day_instances[60], day_62_instance=day_instances[61], day_63_instance=day_instances[62],
                           day_64_instance=day_instances[63], day_65_instance=day_instances[64], day_66_instance=day_instances[65],
                           day_67_instance=day_instances[66], day_68_instance=day_instances[67], day_69_instance=day_instances[68],
                           day_70_instance=day_instances[69], day_71_instance=day_instances[70], day_72_instance=day_instances[71],
                           day_73_instance=day_instances[72], day_74_instance=day_instances[73], day_75_instance=day_instances[74],
                           day_76_instance=day_instances[75], day_77_instance=day_instances[76], day_78_instance=day_instances[77],
                           day_79_instance=day_instances[78], day_80_instance=day_instances[79], day_81_instance=day_instances[80],
                           day_82_instance=day_instances[81], day_83_instance=day_instances[82], day_84_instance=day_instances[83],
                           day_85_instance=day_instances[84], day_86_instance=day_instances[85], day_87_instance=day_instances[86],
                           day_88_instance=day_instances[87], day_89_instance=day_instances[88], day_90_instance=day_instances[89],
                           day_91_instance=day_instances[90], day_92_instance=day_instances[91], day_93_instance=day_instances[92],
                           day_94_instance=day_instances[93], day_95_instance=day_instances[94], day_96_instance=day_instances[95],
                           day_97_instance=day_instances[96], day_98_instance=day_instances[97], day_99_instance=day_instances[98],
                           day_100_instance=day_instances[99],
                           day_1_goal=day_goals[0], day_2_goal=day_goals[1], day_3_goal=day_goals[2],
                           day_4_goal=day_goals[3], day_5_goal=day_goals[4], day_6_goal=day_goals[5],
                           day_7_goal=day_goals[6], day_8_goal=day_goals[7], day_9_goal=day_goals[8],
                           day_10_goal=day_goals[9], day_11_goal=day_goals[10], day_12_goal=day_goals[11],
                           day_13_goal=day_goals[12], day_14_goal=day_goals[13], day_15_goal=day_goals[14],
                           day_16_goal=day_goals[15], day_17_goal=day_goals[16], day_18_goal=day_goals[17],
                           day_19_goal=day_goals[18], day_20_goal=day_goals[19], day_21_goal=day_goals[20],
                           day_22_goal=day_goals[21], day_23_goal=day_goals[22], day_24_goal=day_goals[23],
                           day_25_goal=day_goals[24], day_26_goal=day_goals[25], day_27_goal=day_goals[26],
                           day_28_goal=day_goals[27], day_29_goal=day_goals[28], day_30_goal=day_goals[29],
                           day_31_goal=day_goals[30], day_32_goal=day_goals[31], day_33_goal=day_goals[32],
                           day_34_goal=day_goals[33], day_35_goal=day_goals[34], day_36_goal=day_goals[35],
                           day_37_goal=day_goals[36], day_38_goal=day_goals[37], day_39_goal=day_goals[38],
                           day_40_goal=day_goals[39], day_41_goal=day_goals[40], day_42_goal=day_goals[41],
                           day_43_goal=day_goals[42], day_44_goal=day_goals[43], day_45_goal=day_goals[44],
                           day_46_goal=day_goals[45], day_47_goal=day_goals[46], day_48_goal=day_goals[47],
                           day_49_goal=day_goals[48], day_50_goal=day_goals[49], day_51_goal=day_goals[50],
                           day_52_goal=day_goals[51], day_53_goal=day_goals[52], day_54_goal=day_goals[53],
                           day_55_goal=day_goals[54], day_56_goal=day_goals[55], day_57_goal=day_goals[56],
                           day_58_goal=day_goals[57], day_59_goal=day_goals[58], day_60_goal=day_goals[59],
                           day_61_goal=day_goals[60], day_62_goal=day_goals[61], day_63_goal=day_goals[62],
                           day_64_goal=day_goals[63], day_65_goal=day_goals[64], day_66_goal=day_goals[65],
                           day_67_goal=day_goals[66], day_68_goal=day_goals[67], day_69_goal=day_goals[68],
                           day_70_goal=day_goals[69], day_71_goal=day_goals[70], day_72_goal=day_goals[71],
                           day_73_goal=day_goals[72], day_74_goal=day_goals[73], day_75_goal=day_goals[74],
                           day_76_goal=day_goals[75], day_77_goal=day_goals[76], day_78_goal=day_goals[77],
                           day_79_goal=day_goals[78], day_80_goal=day_goals[79], day_81_goal=day_goals[80],
                           day_82_goal=day_goals[81], day_83_goal=day_goals[82], day_84_goal=day_goals[83],
                           day_85_goal=day_goals[84], day_86_goal=day_goals[85], day_87_goal=day_goals[86],
                           day_88_goal=day_goals[87], day_89_goal=day_goals[88], day_90_goal=day_goals[89],
                           day_91_goal=day_goals[90], day_92_goal=day_goals[91], day_93_goal=day_goals[92],
                           day_94_goal=day_goals[93], day_95_goal=day_goals[94], day_96_goal=day_goals[95],
                           day_97_goal=day_goals[96], day_98_goal=day_goals[97], day_99_goal=day_goals[98],
                           day_100_goal=day_goals[99],
                           )


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response