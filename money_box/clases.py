from flask_login import UserMixin, login_user

from money_box import db, login_manager


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    goal = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.login


class UserAuth(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return UserAuth.query.get(user_id)
