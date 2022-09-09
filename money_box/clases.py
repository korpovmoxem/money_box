from flask_login import UserMixin

from money_box import db, login_manager

class UserAuth(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class DayGoals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    total_goal = db.Column(db.Integer, nullable=False)
    current_sum = db.Column(db.Integer, nullable=False)
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
    new_user_goal = DayGoals(login=user_login, total_goal=goal_target, current_sum=0, day_1=day_goals[0].goal,
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

def update_day_instance(user_login, buttons_list):
    user = DayInstances.query.filter_by(login=user_login).first()
    # Получение накопленной суммы из БД
    ind = buttons_list.index()
    user.day_1 = buttons_list[0] if buttons_list[0] is not None else user.day_1
    user.day_2 = buttons_list[1] if buttons_list[1] is not None else user.day_2
    user.day_3 = buttons_list[2] if buttons_list[2] is not None else user.day_3
    user.day_4 = buttons_list[3] if buttons_list[3] is not None else user.day_4
    user.day_5 = buttons_list[4] if buttons_list[4] is not None else user.day_5
    user.day_6 = buttons_list[5] if buttons_list[5] is not None else user.day_6
    user.day_7 = buttons_list[6] if buttons_list[6] is not None else user.day_7
    user.day_8 = buttons_list[7] if buttons_list[7] is not None else user.day_8
    user.day_9 = buttons_list[8] if buttons_list[8] is not None else user.day_9
    user.day_10 = buttons_list[9] if buttons_list[9] is not None else user.day_10
    user.day_11 = buttons_list[10] if buttons_list[10] is not None else user.day_11
    user.day_12 = buttons_list[11] if buttons_list[11] is not None else user.day_12
    user.day_13 = buttons_list[12] if buttons_list[12] is not None else user.day_13
    user.day_14 = buttons_list[13] if buttons_list[13] is not None else user.day_14
    user.day_15 = buttons_list[14] if buttons_list[14] is not None else user.day_15
    user.day_16 = buttons_list[15] if buttons_list[15] is not None else user.day_16
    user.day_17 = buttons_list[16] if buttons_list[16] is not None else user.day_17
    user.day_18 = buttons_list[17] if buttons_list[17] is not None else user.day_18
    user.day_19 = buttons_list[18] if buttons_list[18] is not None else user.day_19
    user.day_20 = buttons_list[19] if buttons_list[19] is not None else user.day_20
    user.day_21 = buttons_list[20] if buttons_list[20] is not None else user.day_21
    user.day_22 = buttons_list[21] if buttons_list[21] is not None else user.day_22
    user.day_23 = buttons_list[22] if buttons_list[22] is not None else user.day_23
    user.day_24 = buttons_list[23] if buttons_list[23] is not None else user.day_24
    user.day_25 = buttons_list[24] if buttons_list[24] is not None else user.day_25
    user.day_26 = buttons_list[25] if buttons_list[25] is not None else user.day_26
    user.day_27 = buttons_list[26] if buttons_list[26] is not None else user.day_27
    user.day_28 = buttons_list[27] if buttons_list[27] is not None else user.day_28
    user.day_29 = buttons_list[28] if buttons_list[28] is not None else user.day_29
    user.day_30 = buttons_list[29] if buttons_list[29] is not None else user.day_30
    user.day_31 = buttons_list[30] if buttons_list[30] is not None else user.day_31
    user.day_32 = buttons_list[31] if buttons_list[31] is not None else user.day_32
    user.day_33 = buttons_list[32] if buttons_list[32] is not None else user.day_33
    user.day_34 = buttons_list[33] if buttons_list[33] is not None else user.day_34
    user.day_35 = buttons_list[34] if buttons_list[34] is not None else user.day_35
    user.day_36 = buttons_list[35] if buttons_list[35] is not None else user.day_36
    user.day_37 = buttons_list[36] if buttons_list[36] is not None else user.day_37
    user.day_38 = buttons_list[37] if buttons_list[37] is not None else user.day_38
    user.day_39 = buttons_list[38] if buttons_list[38] is not None else user.day_39
    user.day_40 = buttons_list[39] if buttons_list[39] is not None else user.day_40
    user.day_41 = buttons_list[40] if buttons_list[40] is not None else user.day_41
    user.day_42 = buttons_list[41] if buttons_list[41] is not None else user.day_42
    user.day_43 = buttons_list[42] if buttons_list[42] is not None else user.day_43
    user.day_44 = buttons_list[43] if buttons_list[43] is not None else user.day_44
    user.day_45 = buttons_list[44] if buttons_list[44] is not None else user.day_45
    user.day_46 = buttons_list[45] if buttons_list[45] is not None else user.day_46
    user.day_47 = buttons_list[46] if buttons_list[46] is not None else user.day_47
    user.day_48 = buttons_list[47] if buttons_list[47] is not None else user.day_48
    user.day_49 = buttons_list[48] if buttons_list[48] is not None else user.day_49
    user.day_50 = buttons_list[49] if buttons_list[49] is not None else user.day_50
    user.day_51 = buttons_list[50] if buttons_list[50] is not None else user.day_51
    user.day_52 = buttons_list[51] if buttons_list[51] is not None else user.day_52
    user.day_53 = buttons_list[52] if buttons_list[52] is not None else user.day_53
    user.day_54 = buttons_list[53] if buttons_list[53] is not None else user.day_54
    user.day_55 = buttons_list[54] if buttons_list[54] is not None else user.day_55
    user.day_56 = buttons_list[55] if buttons_list[55] is not None else user.day_56
    user.day_57 = buttons_list[56] if buttons_list[56] is not None else user.day_57
    user.day_58 = buttons_list[57] if buttons_list[57] is not None else user.day_58
    user.day_59 = buttons_list[58] if buttons_list[58] is not None else user.day_59
    user.day_60 = buttons_list[59] if buttons_list[59] is not None else user.day_60
    user.day_61 = buttons_list[60] if buttons_list[60] is not None else user.day_61
    user.day_62 = buttons_list[61] if buttons_list[61] is not None else user.day_62
    user.day_63 = buttons_list[62] if buttons_list[62] is not None else user.day_63
    user.day_64 = buttons_list[63] if buttons_list[63] is not None else user.day_64
    user.day_65 = buttons_list[64] if buttons_list[64] is not None else user.day_65
    user.day_66 = buttons_list[65] if buttons_list[65] is not None else user.day_66
    user.day_67 = buttons_list[66] if buttons_list[66] is not None else user.day_67
    user.day_68 = buttons_list[67] if buttons_list[67] is not None else user.day_68
    user.day_69 = buttons_list[68] if buttons_list[68] is not None else user.day_69
    user.day_70 = buttons_list[69] if buttons_list[69] is not None else user.day_70
    user.day_71 = buttons_list[70] if buttons_list[70] is not None else user.day_71
    user.day_72 = buttons_list[71] if buttons_list[71] is not None else user.day_72
    user.day_73 = buttons_list[72] if buttons_list[72] is not None else user.day_73
    user.day_74 = buttons_list[73] if buttons_list[73] is not None else user.day_74
    user.day_75 = buttons_list[74] if buttons_list[74] is not None else user.day_75
    user.day_76 = buttons_list[75] if buttons_list[75] is not None else user.day_76
    user.day_77 = buttons_list[76] if buttons_list[76] is not None else user.day_77
    user.day_78 = buttons_list[77] if buttons_list[77] is not None else user.day_78
    user.day_79 = buttons_list[78] if buttons_list[78] is not None else user.day_79
    user.day_80 = buttons_list[79] if buttons_list[79] is not None else user.day_80
    user.day_81 = buttons_list[80] if buttons_list[80] is not None else user.day_81
    user.day_82 = buttons_list[81] if buttons_list[81] is not None else user.day_82
    user.day_83 = buttons_list[82] if buttons_list[82] is not None else user.day_83
    user.day_84 = buttons_list[83] if buttons_list[83] is not None else user.day_84
    user.day_85 = buttons_list[84] if buttons_list[84] is not None else user.day_85
    user.day_86 = buttons_list[85] if buttons_list[85] is not None else user.day_86
    user.day_87 = buttons_list[86] if buttons_list[86] is not None else user.day_87
    user.day_88 = buttons_list[87] if buttons_list[87] is not None else user.day_88
    user.day_89 = buttons_list[88] if buttons_list[88] is not None else user.day_89
    user.day_90 = buttons_list[89] if buttons_list[89] is not None else user.day_90
    user.day_91 = buttons_list[90] if buttons_list[90] is not None else user.day_91
    user.day_92 = buttons_list[91] if buttons_list[91] is not None else user.day_92
    user.day_93 = buttons_list[92] if buttons_list[92] is not None else user.day_93
    user.day_94 = buttons_list[93] if buttons_list[93] is not None else user.day_94
    user.day_95 = buttons_list[94] if buttons_list[94] is not None else user.day_95
    user.day_96 = buttons_list[95] if buttons_list[95] is not None else user.day_96
    user.day_97 = buttons_list[96] if buttons_list[96] is not None else user.day_97
    user.day_98 = buttons_list[97] if buttons_list[97] is not None else user.day_98
    user.day_99 = buttons_list[98] if buttons_list[98] is not None else user.day_99
    user.day_100 = buttons_list[99] if buttons_list[99] is not None else user.day_100

    db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return UserAuth.query.get(user_id)

