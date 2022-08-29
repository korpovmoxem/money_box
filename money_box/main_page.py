from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user

from money_box import app, db
from money_box.clases import UserAuth


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/info')
def info_page():
    return render_template('info_page.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration_page():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Необходимо заполнить все поля')
            return render_template('registration_page.html')
        elif password != password2 or password == '' or password2 == '':
            flash('Пароли не совпадают')
            return render_template('registration_page.html')
        else:
            if len(password) < 6:
                flash('Длина пароля должна быть не меньше 6 символов')

            hash_password = generate_password_hash(password)
            new_user = UserAuth(login=login, password=hash_password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page'))
        return render_template('registration_page.html')
    else:
        return render_template('registration_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
         user = UserAuth.query.filter_by(login=login).first()

         if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')

            return redirect(url_for('money_box'))

         else:
            flash('Логин или пароль неверны')
    else:
        flash('Необходимо заполнить поля "Логин" и "Пароль"')
    return render_template('login_page.html')


@app.route('/logout')
@login_required
def login_out():
    logout_user()
    return redirect((url_for('main_page')))


@app.route('/money_box')
@login_required
def money_box():
    return render_template('money_box.html')


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response