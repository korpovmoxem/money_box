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

class DayInstances(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
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
        days.append(DayGoal(int(day_goal - goal_tail)))

    return(days)

def fill_day_instances(user_login):
    new_user_instances = DayInstances(login=user_login)
    db.session.add(new_user_instances)
    db.session.commit()

def fill_days_db(user_login, day_goals, goal_target):
    new_user_goal = DayGoals(login=user_login, total_goal=goal_target, day_1=day_goals[0].goal,
                             day_2=day_goals[1].goal, day_3=day_goals[2].goal, day_4=day_goals[3].goal,
                             day_5=day_goals[4].goal, day_6=day_goals[5].goal, day_7=day_goals[6].goal,
                             day_8=day_goals[7].goal, day_9=day_goals[8].goal, day_10=day_goals[9].goal,
                             day_11=day_goals[10].goal, day_12=day_goals[11].goal, day_13=day_goals[12].goal,
                             day_14=day_goals[13].goal, day_15=day_goals[14].goal, day_16=day_goals[15].goal,
                             day_17=day_goals[16].goal, day_18=day_goals[17].goal, day_19=day_goals[18].goal,
                             day_20=day_goals[19].goal, day_21=day_goals[20].goal, day_22=day_goals[21].goal,
                             day_23=day_goals[22].goal, day_24=day_goals[23].goal, day_25=day_goals[24].goal,
                             day_26=day_goals[25].goal, day_27=day_goals[26].goal, day_28=day_goals[27].goal, day_29=day_goals[28].goal,
                             day_30=day_goals[29].goal, day_31=day_goals[30].goal, day_32=day_goals[31].goal,
                             day_33=day_goals[32].goal, day_34=day_goals[33].goal, day_35=day_goals[34].goal,
                             day_36=day_goals[35].goal, day_37=day_goals[36].goal, day_38=day_goals[37].goal,
                             day_39=day_goals[38].goal, day_40=day_goals[39].goal, day_41=day_goals[40].goal,
                             day_42=day_goals[41].goal, day_43=day_goals[42].goal, day_44=day_goals[43].goal,
                             day_45=day_goals[44].goal, day_46=day_goals[45].goal, day_47=day_goals[46].goal,
                             day_48=day_goals[47].goal, day_49=day_goals[48].goal, day_50=day_goals[49].goal,
                             day_51=day_goals[50].goal, day_52=day_goals[51].goal, day_53=day_goals[52].goal, day_54=day_goals[53].goal,
                             day_55=day_goals[54].goal, day_56=day_goals[55].goal, day_57=day_goals[56].goal,
                             day_58=day_goals[57].goal, day_59=day_goals[58].goal, day_60=day_goals[59].goal,
                             day_61=day_goals[60].goal, day_62=day_goals[61].goal, day_63=day_goals[62].goal,
                             day_64=day_goals[63].goal, day_65=day_goals[64].goal, day_66=day_goals[65].goal,
                             day_67=day_goals[66].goal, day_68=day_goals[67].goal, day_69=day_goals[68].goal,
                             day_70=day_goals[69].goal, day_71=day_goals[70].goal, day_72=day_goals[71].goal,
                             day_73=day_goals[72].goal, day_74=day_goals[73].goal, day_75=day_goals[74].goal,
                             day_76=day_goals[75].goal, day_77=day_goals[76].goal, day_78=day_goals[77].goal, day_79=day_goals[78].goal,
                             day_80=day_goals[79].goal, day_81=day_goals[80].goal, day_82=day_goals[81].goal,
                             day_83=day_goals[82].goal, day_84=day_goals[83].goal, day_85=day_goals[84].goal,
                             day_86=day_goals[85].goal, day_87=day_goals[86].goal, day_88=day_goals[87].goal,
                             day_89=day_goals[88].goal, day_90=day_goals[89].goal, day_91=day_goals[90].goal,
                             day_92=day_goals[91].goal, day_93=day_goals[92].goal, day_94=day_goals[93].goal,
                             day_95=day_goals[94].goal, day_96=day_goals[95].goal, day_97=day_goals[96].goal,
                             day_98=day_goals[97].goal, day_99=day_goals[98].goal, day_100=day_goals[99].goal,)
    db.session.add(new_user_goal)
    db.session.commit()

def get_day_goals(user_login):
    user = DayGoals.query.filter_by(login=user_login).first()
    return [
        user.day_1, user.day_2, user.day_3, user.day_4, user.day_5, user.day_6, user.day_7, user.day_8,
        user.day_9, user.day_10, user.day_11, user.day_12, user.day_13, user.day_14, user.day_15, user.day_16,
        user.day_17, user.day_18, user.day_19, user.day_20, user.day_21, user.day_22, user.day_23, user.day_24,
        user.day_25, user.day_26, user.day_27, user.day_28, user.day_29, user.day_30, user.day_31, user.day_32,
        user.day_33, user.day_34, user.day_35, user.day_36, user.day_37, user.day_38, user.day_39, user.day_40,
        user.day_41, user.day_42, user.day_43, user.day_44, user.day_45, user.day_46, user.day_47, user.day_48,
        user.day_49, user.day_50, user.day_51, user.day_52, user.day_53, user.day_54, user.day_55, user.day_56,
        user.day_57,
        user.day_58, user.day_59, user.day_60, user.day_61, user.day_62, user.day_63, user.day_64, user.day_65,
        user.day_66,
        user.day_67, user.day_68, user.day_69, user.day_70, user.day_71, user.day_72, user.day_73, user.day_74,
        user.day_75, user.day_76, user.day_77, user.day_78, user.day_79, user.day_80, user.day_81, user.day_82,
        user.day_83, user.day_84, user.day_85, user.day_86, user.day_87, user.day_88, user.day_89, user.day_90,
        user.day_91, user.day_92, user.day_93, user.day_94, user.day_95, user.day_96, user.day_97, user.day_98,
        user.day_99, user.day_100
    ]

def get_day_instances(user_login):
    user = DayInstances.query.filter_by(login=user_login).first()
    return [
        user.day_1, user.day_2, user.day_3, user.day_4, user.day_5, user.day_6, user.day_7, user.day_8,
        user.day_9, user.day_10, user.day_11, user.day_12, user.day_13, user.day_14, user.day_15, user.day_16,
        user.day_17, user.day_18, user.day_19, user.day_20, user.day_21, user.day_22, user.day_23, user.day_24,
        user.day_25, user.day_26, user.day_27, user.day_28, user.day_29, user.day_30, user.day_31, user.day_32,
        user.day_33, user.day_34, user.day_35, user.day_36, user.day_37, user.day_38, user.day_39, user.day_40,
        user.day_41, user.day_42, user.day_43, user.day_44, user.day_45, user.day_46, user.day_47, user.day_48,
        user.day_49, user.day_50, user.day_51, user.day_52, user.day_53, user.day_54, user.day_55, user.day_56, user.day_57,
        user.day_58, user.day_59, user.day_60, user.day_61, user.day_62, user.day_63, user.day_64, user.day_65, user.day_66,
        user.day_67,user.day_68, user.day_69, user.day_70, user.day_71, user.day_72, user.day_73, user.day_74,
        user.day_75,user.day_76, user.day_77, user.day_78, user.day_79, user.day_80, user.day_81, user.day_82,
        user.day_83,user.day_84, user.day_85, user.day_86, user.day_87, user.day_88, user.day_89, user.day_90,
        user.day_91,user.day_92, user.day_93, user.day_94, user.day_95, user.day_96, user.day_97, user.day_98,
        user.day_99, user.day_100
    ]


class UserAuth(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return UserAuth.query.get(user_id)

