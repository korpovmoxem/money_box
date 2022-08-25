from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user

from money_box import app, db
from money_box.clases import UserAuth


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/info')
def info_page():
    return render_template('info_page.html')


@app.route('/registration')
def registration_page():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Необходимо заполнить все поля')
        elif password != password2:
            flash('Пароли не совпадают')
        else:
            hash_password = generate_password_hash(password)
            new_user = UserAuth(login=login, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page.html'))
    else:
        return render_template('registration_page.html')


@app.route('/login')
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
         user = UserAuth.query.filter_by(login=login).first()

         if check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')

            redirect(next_page)
         else:
            flash('Логин или пароль неверны')
    else:
        flash('Необходимо заполнить поля "Логин" и "Пароль"'
              '')
        return render_template('login_page.html')


@app.route('/auth_out')
def login_out():
    pass