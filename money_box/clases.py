from flask_login import UserMixin

from money_box import db, login_manager


class DayGoals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    total_goal = db.Column(db.Integer, nullable=False)
    day_1 = db.Column(db.Integer)
    day_2 = db.Column(db.Integer)
    day_3 = db.Column(db.Integer)
    day_4 = db.Column(db.Integer)
    day_5 = db.Column(db.Integer)
    day_6 = db.Column(db.Integer)
    day_7 = db.Column(db.Integer)
    day_8 = db.Column(db.Integer)
    day_9 = db.Column(db.Integer)
    day_10 = db.Column(db.Integer)
    day_11 = db.Column(db.Integer)
    day_12 = db.Column(db.Integer)
    day_13 = db.Column(db.Integer)
    day_14 = db.Column(db.Integer)
    day_15 = db.Column(db.Integer)
    day_16 = db.Column(db.Integer)
    day_17 = db.Column(db.Integer)
    day_18 = db.Column(db.Integer)
    day_19 = db.Column(db.Integer)
    day_20 = db.Column(db.Integer)
    day_21 = db.Column(db.Integer)
    day_22 = db.Column(db.Integer)
    day_23 = db.Column(db.Integer)
    day_24 = db.Column(db.Integer)
    day_25 = db.Column(db.Integer)
    day_26 = db.Column(db.Integer)
    day_27 = db.Column(db.Integer)
    day_28 = db.Column(db.Integer)
    day_29 = db.Column(db.Integer)
    day_30 = db.Column(db.Integer)
    day_31 = db.Column(db.Integer)
    day_31 = db.Column(db.Integer)
    day_32 = db.Column(db.Integer)
    day_33 = db.Column(db.Integer)
    day_34 = db.Column(db.Integer)
    day_35 = db.Column(db.Integer)
    day_36 = db.Column(db.Integer)
    day_37 = db.Column(db.Integer)
    day_38 = db.Column(db.Integer)
    day_39 = db.Column(db.Integer)
    day_40 = db.Column(db.Integer)
    day_41 = db.Column(db.Integer)
    day_42 = db.Column(db.Integer)
    day_43 = db.Column(db.Integer)
    day_44 = db.Column(db.Integer)
    day_45 = db.Column(db.Integer)
    day_46 = db.Column(db.Integer)
    day_47 = db.Column(db.Integer)
    day_48 = db.Column(db.Integer)
    day_49 = db.Column(db.Integer)
    day_50 = db.Column(db.Integer)
    day_51 = db.Column(db.Integer)
    day_52 = db.Column(db.Integer)
    day_53 = db.Column(db.Integer)
    day_54 = db.Column(db.Integer)
    day_55 = db.Column(db.Integer)
    day_56 = db.Column(db.Integer)
    day_57 = db.Column(db.Integer)
    day_58 = db.Column(db.Integer)
    day_59 = db.Column(db.Integer)
    day_60 = db.Column(db.Integer)
    day_61 = db.Column(db.Integer)
    day_62 = db.Column(db.Integer)
    day_63 = db.Column(db.Integer)
    day_64 = db.Column(db.Integer)
    day_65 = db.Column(db.Integer)
    day_66 = db.Column(db.Integer)
    day_67 = db.Column(db.Integer)
    day_68 = db.Column(db.Integer)
    day_69 = db.Column(db.Integer)
    day_70 = db.Column(db.Integer)
    day_71 = db.Column(db.Integer)
    day_72 = db.Column(db.Integer)
    day_73 = db.Column(db.Integer)
    day_74 = db.Column(db.Integer)
    day_75 = db.Column(db.Integer)
    day_76 = db.Column(db.Integer)
    day_77 = db.Column(db.Integer)
    day_78 = db.Column(db.Integer)
    day_79 = db.Column(db.Integer)
    day_80 = db.Column(db.Integer)
    day_81 = db.Column(db.Integer)
    day_82 = db.Column(db.Integer)
    day_83 = db.Column(db.Integer)
    day_84 = db.Column(db.Integer)
    day_85 = db.Column(db.Integer)
    day_86 = db.Column(db.Integer)
    day_87 = db.Column(db.Integer)
    day_88 = db.Column(db.Integer)
    day_89 = db.Column(db.Integer)
    day_90 = db.Column(db.Integer)
    day_91 = db.Column(db.Integer)
    day_92 = db.Column(db.Integer)
    day_93 = db.Column(db.Integer)
    day_94 = db.Column(db.Integer)
    day_95 = db.Column(db.Integer)
    day_96 = db.Column(db.Integer)
    day_97 = db.Column(db.Integer)
    day_98 = db.Column(db.Integer)
    day_99 = db.Column(db.Integer)
    day_100 = db.Column(db.Integer)








    def __repr__(self):
        return '<User %r>' % self.login


class UserAuth(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return UserAuth.query.get(user_id)


def create_day_goals(goal):
    """
    Сумма должна быть кратна 5000
    """
    goal = int(goal)

    class DayGoal:
        day_number = 0

        def __init__(self, goal):
            DayGoal.day_number += 1
            self.day_number = DayGoal.day_number
            self.goal = goal

    days = []
    const_goal = 50_000
    const_step_value = 10
    step_value_multiplier = goal / const_goal
    day_goal = 0
    goal_tail = (goal / 100) / 100
    day_step_value = const_step_value * step_value_multiplier

    for day in range(100):
        day_goal += day_step_value
        days.append(DayGoal(day_goal - goal_tail))

