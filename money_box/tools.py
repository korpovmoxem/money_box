from datetime import datetime

from flask_login import UserMixin

from money_box import db, login_manager


class UserAuth(db.Model, UserMixin):
    """
    БД с данными пользователей
    """
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


class DayGoals(db.Model):
    """
    БД с целями пользователей, текущей накопленной суммой и значениями для кнопок
    """
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
    """
    БД с состояниями кнопок (нажата или нет)
    """
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


class UserLogs(db.Model):
    """
    БД с логами пользователя (история нажатия кнопок)
    """
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    log_1 = db.Column(db.String(128))
    log_2 = db.Column(db.String(128))
    log_3 = db.Column(db.String(128))
    log_4 = db.Column(db.String(128))
    log_5 = db.Column(db.String(128))
    log_6 = db.Column(db.String(128))
    log_7 = db.Column(db.String(128))
    log_8 = db.Column(db.String(128))
    log_9 = db.Column(db.String(128))
    log_10 = db.Column(db.String(128))
    log_11 = db.Column(db.String(128))
    log_12 = db.Column(db.String(128))
    log_13 = db.Column(db.String(128))
    log_14 = db.Column(db.String(128))
    log_15 = db.Column(db.String(128))
    log_16 = db.Column(db.String(128))
    log_17 = db.Column(db.String(128))
    log_18 = db.Column(db.String(128))
    log_19 = db.Column(db.String(128))
    log_20 = db.Column(db.String(128))
    log_21 = db.Column(db.String(128))
    log_22 = db.Column(db.String(128))
    log_23 = db.Column(db.String(128))
    log_24 = db.Column(db.String(128))
    log_25 = db.Column(db.String(128))
    log_26 = db.Column(db.String(128))
    log_27 = db.Column(db.String(128))
    log_28 = db.Column(db.String(128))
    log_29 = db.Column(db.String(128))
    log_30 = db.Column(db.String(128))
    log_31 = db.Column(db.String(128))
    log_32 = db.Column(db.String(128))
    log_33 = db.Column(db.String(128))
    log_34 = db.Column(db.String(128))
    log_35 = db.Column(db.String(128))
    log_36 = db.Column(db.String(128))
    log_37 = db.Column(db.String(128))
    log_38 = db.Column(db.String(128))
    log_39 = db.Column(db.String(128))
    log_40 = db.Column(db.String(128))
    log_41 = db.Column(db.String(128))
    log_42 = db.Column(db.String(128))
    log_43 = db.Column(db.String(128))
    log_44 = db.Column(db.String(128))
    log_45 = db.Column(db.String(128))
    log_46 = db.Column(db.String(128))
    log_47 = db.Column(db.String(128))
    log_48 = db.Column(db.String(128))
    log_49 = db.Column(db.String(128))
    log_50 = db.Column(db.String(128))
    log_51 = db.Column(db.String(128))
    log_52 = db.Column(db.String(128))
    log_53 = db.Column(db.String(128))
    log_54 = db.Column(db.String(128))
    log_55 = db.Column(db.String(128))
    log_56 = db.Column(db.String(128))
    log_57 = db.Column(db.String(128))
    log_58 = db.Column(db.String(128))
    log_59 = db.Column(db.String(128))
    log_60 = db.Column(db.String(128))
    log_61 = db.Column(db.String(128))
    log_62 = db.Column(db.String(128))
    log_63 = db.Column(db.String(128))
    log_64 = db.Column(db.String(128))
    log_65 = db.Column(db.String(128))
    log_66 = db.Column(db.String(128))
    log_67 = db.Column(db.String(128))
    log_68 = db.Column(db.String(128))
    log_69 = db.Column(db.String(128))
    log_70 = db.Column(db.String(128))
    log_71 = db.Column(db.String(128))
    log_72 = db.Column(db.String(128))
    log_73 = db.Column(db.String(128))
    log_74 = db.Column(db.String(128))
    log_75 = db.Column(db.String(128))
    log_76 = db.Column(db.String(128))
    log_77 = db.Column(db.String(128))
    log_78 = db.Column(db.String(128))
    log_79 = db.Column(db.String(128))
    log_80 = db.Column(db.String(128))
    log_81 = db.Column(db.String(128))
    log_82 = db.Column(db.String(128))
    log_83 = db.Column(db.String(128))
    log_84 = db.Column(db.String(128))
    log_85 = db.Column(db.String(128))
    log_86 = db.Column(db.String(128))
    log_87 = db.Column(db.String(128))
    log_88 = db.Column(db.String(128))
    log_89 = db.Column(db.String(128))
    log_90 = db.Column(db.String(128))
    log_91 = db.Column(db.String(128))
    log_92 = db.Column(db.String(128))
    log_93 = db.Column(db.String(128))
    log_94 = db.Column(db.String(128))
    log_95 = db.Column(db.String(128))
    log_96 = db.Column(db.String(128))
    log_97 = db.Column(db.String(128))
    log_98 = db.Column(db.String(128))
    log_99 = db.Column(db.String(128))
    log_100 = db.Column(db.String(128))


def write_log(login, value):
    """
    Запись логов нажатия на кнопки в БД
    :param login: user.login
    :param value: Значение кнопки
    """
    user = UserLogs.query.filter_by(login=login).first()
    log = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}: {value}"
    # Проверка дублирующего нажатия
    user_logs = [
        user.log_1, user.log_2, user.log_3, user.log_4, user.log_5, user.log_6, user.log_7, user.log_8, user.log_9,
        user.log_10, user.log_11, user.log_12, user.log_13, user.log_14, user.log_15, user.log_16, user.log_17,
        user.log_18, user.log_19, user.log_20, user.log_21, user.log_22, user.log_23, user.log_24, user.log_25,
        user.log_26, user.log_27, user.log_28, user.log_29, user.log_30, user.log_31, user.log_32, user.log_33,
        user.log_34, user.log_35, user.log_36, user.log_37, user.log_38, user.log_39, user.log_40, user.log_41,
        user.log_42, user.log_43, user.log_44, user.log_45, user.log_46, user.log_47, user.log_48, user.log_49,
        user.log_50, user.log_51, user.log_52, user.log_53, user.log_54, user.log_55, user.log_56, user.log_57,
        user.log_58, user.log_59, user.log_60, user.log_61, user.log_62, user.log_63, user.log_64, user.log_65,
        user.log_66, user.log_67, user.log_68, user.log_69, user.log_70, user.log_71, user.log_72, user.log_73,
        user.log_74, user.log_75, user.log_76, user.log_77, user.log_78, user.log_79, user.log_80, user.log_81,
        user.log_82, user.log_83, user.log_84, user.log_85, user.log_86, user.log_87, user.log_88, user.log_89,
        user.log_90, user.log_91, user.log_92, user.log_93, user.log_94, user.log_95, user.log_96, user.log_97,
        user.log_98, user.log_99, user.log_100
    ]
    # Запись лога
    for user_log in user_logs:
        if user_log == log:
            return
    if not user.log_1:
        user.log_1 = log
        db.session.commit()
        return
    elif not user.log_2:
        user.log_2 = log
        db.session.commit()
        return
    elif not user.log_3:
        user.log_3 = log
        db.session.commit()
        return
    elif not user.log_4:
        user.log_4 = log
        db.session.commit()
        return
    elif not user.log_5:
        user.log_5 = log
        db.session.commit()
        return
    elif not user.log_6:
        user.log_6 = log
        db.session.commit()
        return
    elif not user.log_7:
        user.log_7 = log
        db.session.commit()
        return
    elif not user.log_8:
        user.log_8 = log
        db.session.commit()
        return
    elif not user.log_9:
        user.log_9 = log
        db.session.commit()
        return
    elif not user.log_10:
        user.log_10 = log
        db.session.commit()
        return
    elif not user.log_11:
        user.log_11 = log
        db.session.commit()
        return
    elif not user.log_12:
        user.log_12 = log
        db.session.commit()
        return
    elif not user.log_13:
        user.log_13 = log
        db.session.commit()
        return
    elif not user.log_14:
        user.log_14 = log
        db.session.commit()
        return
    elif not user.log_15:
        user.log_15 = log
        db.session.commit()
        return
    elif not user.log_16:
        user.log_16 = log
        db.session.commit()
        return
    elif not user.log_17:
        user.log_17 = log
        db.session.commit()
        return
    elif not user.log_18:
        user.log_18 = log
        db.session.commit()
        return
    elif not user.log_19:
        user.log_19 = log
        db.session.commit()
        return
    elif not user.log_20:
        user.log_20 = log
        db.session.commit()
        return
    elif not user.log_21:
        user.log_21 = log
        db.session.commit()
        return
    elif not user.log_22:
        user.log_22 = log
        db.session.commit()
        return
    elif not user.log_23:
        user.log_23 = log
        db.session.commit()
        return
    elif not user.log_24:
        user.log_24 = log
        db.session.commit()
        return
    elif not user.log_25:
        user.log_25 = log
        db.session.commit()
        return
    elif not user.log_26:
        user.log_26 = log
        db.session.commit()
        return
    elif not user.log_27:
        user.log_27 = log
        db.session.commit()
        return
    elif not user.log_28:
        user.log_28 = log
        db.session.commit()
        return
    elif not user.log_29:
        user.log_29 = log
        db.session.commit()
        return
    elif not user.log_30:
        user.log_30 = log
        db.session.commit()
        return
    elif not user.log_31:
        user.log_31 = log
        db.session.commit()
        return
    elif not user.log_32:
        user.log_32 = log
        db.session.commit()
        return
    elif not user.log_33:
        user.log_33 = log
        db.session.commit()
        return
    elif not user.log_34:
        user.log_34 = log
        db.session.commit()
        return
    elif not user.log_35:
        user.log_35 = log
        db.session.commit()
        return
    elif not user.log_36:
        user.log_36 = log
        db.session.commit()
        return
    elif not user.log_37:
        user.log_37 = log
        db.session.commit()
        return
    elif not user.log_38:
        user.log_38 = log
        db.session.commit()
        return
    elif not user.log_39:
        user.log_39 = log
        db.session.commit()
        return
    elif not user.log_40:
        user.log_40 = log
        db.session.commit()
        return
    elif not user.log_41:
        user.log_41 = log
        db.session.commit()
        return
    elif not user.log_42:
        user.log_42 = log
        db.session.commit()
        return
    elif not user.log_43:
        user.log_43 = log
        db.session.commit()
        return
    elif not user.log_44:
        user.log_44 = log
        db.session.commit()
        return
    elif not user.log_45:
        user.log_45 = log
        db.session.commit()
        return
    elif not user.log_46:
        user.log_46 = log
        db.session.commit()
        return
    elif not user.log_47:
        user.log_47 = log
        db.session.commit()
        return
    elif not user.log_48:
        user.log_48 = log
        db.session.commit()
        return
    elif not user.log_49:
        user.log_49 = log
        db.session.commit()
        return
    elif not user.log_50:
        user.log_50 = log
        db.session.commit()
        return
    elif not user.log_51:
        user.log_51 = log
        db.session.commit()
        return
    elif not user.log_52:
        user.log_52 = log
        db.session.commit()
        return
    elif not user.log_53:
        user.log_53 = log
        db.session.commit()
        return
    elif not user.log_54:
        user.log_54 = log
        db.session.commit()
        return
    elif not user.log_55:
        user.log_55 = log
        db.session.commit()
        return
    elif not user.log_56:
        user.log_56 = log
        db.session.commit()
        return
    elif not user.log_57:
        user.log_57 = log
        db.session.commit()
        return
    elif not user.log_58:
        user.log_58 = log
        db.session.commit()
        return
    elif not user.log_59:
        user.log_59 = log
        db.session.commit()
        return
    elif not user.log_60:
        user.log_60 = log
        db.session.commit()
        return
    elif not user.log_61:
        user.log_61 = log
        db.session.commit()
        return
    elif not user.log_62:
        user.log_62 = log
        db.session.commit()
        return
    elif not user.log_63:
        user.log_63 = log
        db.session.commit()
        return
    elif not user.log_64:
        user.log_64 = log
        db.session.commit()
        return
    elif not user.log_65:
        user.log_65 = log
        db.session.commit()
        return
    elif not user.log_66:
        user.log_66 = log
        db.session.commit()
        return
    elif not user.log_67:
        user.log_67 = log
        db.session.commit()
        return
    elif not user.log_68:
        user.log_68 = log
        db.session.commit()
        return
    elif not user.log_69:
        user.log_69 = log
        db.session.commit()
        return
    elif not user.log_70:
        user.log_70 = log
        db.session.commit()
        return
    elif not user.log_71:
        user.log_71 = log
        db.session.commit()
        return
    elif not user.log_72:
        user.log_72 = log
        db.session.commit()
        return
    elif not user.log_73:
        user.log_73 = log
        db.session.commit()
        return
    elif not user.log_74:
        user.log_74 = log
        db.session.commit()
        return
    elif not user.log_75:
        user.log_75 = log
        db.session.commit()
        return
    elif not user.log_76:
        user.log_76 = log
        db.session.commit()
        return
    elif not user.log_77:
        user.log_77 = log
        db.session.commit()
        return
    elif not user.log_78:
        user.log_78 = log
        db.session.commit()
        return
    elif not user.log_79:
        user.log_79 = log
        db.session.commit()
        return
    elif not user.log_80:
        user.log_80 = log
        db.session.commit()
        return
    elif not user.log_81:
        user.log_81 = log
        db.session.commit()
        return
    elif not user.log_82:
        user.log_82 = log
        db.session.commit()
        return
    elif not user.log_83:
        user.log_83 = log
        db.session.commit()
        return
    elif not user.log_84:
        user.log_84 = log
        db.session.commit()
        return
    elif not user.log_85:
        user.log_85 = log
        db.session.commit()
        return
    elif not user.log_86:
        user.log_86 = log
        db.session.commit()
        return
    elif not user.log_87:
        user.log_87 = log
        db.session.commit()
        return
    elif not user.log_88:
        user.log_88 = log
        db.session.commit()
        return
    elif not user.log_89:
        user.log_89 = log
        db.session.commit()
        return
    elif not user.log_90:
        user.log_90 = log
        db.session.commit()
        return
    elif not user.log_91:
        user.log_91 = log
        db.session.commit()
        return
    elif not user.log_92:
        user.log_92 = log
        db.session.commit()
        return
    elif not user.log_93:
        user.log_93 = log
        db.session.commit()
        return
    elif not user.log_94:
        user.log_94 = log
        db.session.commit()
        return
    elif not user.log_95:
        user.log_95 = log
        db.session.commit()
        return
    elif not user.log_96:
        user.log_96 = log
        db.session.commit()
        return
    elif not user.log_97:
        user.log_97 = log
        db.session.commit()
        return
    elif not user.log_98:
        user.log_98 = log
        db.session.commit()
        return
    elif not user.log_99:
        user.log_99 = log
        db.session.commit()
        return
    elif not user.log_100:
        user.log_100 = log
        db.session.commit()
        return


def clear_logs(login):
    """
    Очищение строки БД с логами
    :param login: user.login
    """
    user = UserLogs.query.filter_by(login=login).first()
    user.log_1 = None
    user.log_2 = None
    user.log_3 = None
    user.log_4 = None
    user.log_5 = None
    user.log_6 = None
    user.log_7 = None
    user.log_8 = None
    user.log_9 = None
    user.log_10 = None
    user.log_11 = None
    user.log_12 = None
    user.log_13 = None
    user.log_14 = None
    user.log_15 = None
    user.log_16 = None
    user.log_17 = None
    user.log_18 = None
    user.log_19 = None
    user.log_20 = None
    user.log_21 = None
    user.log_22 = None
    user.log_23 = None
    user.log_24 = None
    user.log_25 = None
    user.log_26 = None
    user.log_27 = None
    user.log_28 = None
    user.log_29 = None
    user.log_30 = None
    user.log_31 = None
    user.log_32 = None
    user.log_33 = None
    user.log_34 = None
    user.log_35 = None
    user.log_36 = None
    user.log_37 = None
    user.log_38 = None
    user.log_39 = None
    user.log_40 = None
    user.log_41 = None
    user.log_42 = None
    user.log_43 = None
    user.log_44 = None
    user.log_45 = None
    user.log_46 = None
    user.log_47 = None
    user.log_48 = None
    user.log_49 = None
    user.log_50 = None
    user.log_51 = None
    user.log_52 = None
    user.log_53 = None
    user.log_54 = None
    user.log_55 = None
    user.log_56 = None
    user.log_57 = None
    user.log_58 = None
    user.log_59 = None
    user.log_60 = None
    user.log_61 = None
    user.log_62 = None
    user.log_63 = None
    user.log_64 = None
    user.log_65 = None
    user.log_66 = None
    user.log_67 = None
    user.log_68 = None
    user.log_69 = None
    user.log_70 = None
    user.log_71 = None
    user.log_72 = None
    user.log_73 = None
    user.log_74 = None
    user.log_75 = None
    user.log_76 = None
    user.log_77 = None
    user.log_78 = None
    user.log_79 = None
    user.log_80 = None
    user.log_81 = None
    user.log_82 = None
    user.log_83 = None
    user.log_84 = None
    user.log_85 = None
    user.log_86 = None
    user.log_87 = None
    user.log_88 = None
    user.log_89 = None
    user.log_90 = None
    user.log_91 = None
    user.log_92 = None
    user.log_93 = None
    user.log_94 = None
    user.log_95 = None
    user.log_96 = None
    user.log_97 = None
    user.log_98 = None
    user.log_99 = None
    user.log_100 = None
    db.session.commit()


def get_logs(login) -> list:
    """
    Получение логов для отображение в HTML
    :param login: user.login
    :return: List с логами пользователя
    """
    user = UserLogs.query.filter_by(login=login).first()
    # Создание записи о пользователе в БД
    if not user:
        new_user_logs = UserLogs(login=login)
        db.session.add(new_user_logs)
        db.session.commit()
        user = UserLogs.query.filter_by(login=login).first()
    user = UserLogs.query.filter_by(login=login).first()
    filtred_user_logs = []
    user_logs = [
        user.log_1, user.log_2, user.log_3, user.log_4, user.log_5, user.log_6, user.log_7, user.log_8, user.log_9,
        user.log_10, user.log_11, user.log_12, user.log_13, user.log_14, user.log_15, user.log_16, user.log_17,
        user.log_18, user.log_19, user.log_20, user.log_21, user.log_22, user.log_23, user.log_24, user.log_25,
        user.log_26, user.log_27, user.log_28, user.log_29, user.log_30, user.log_31, user.log_32, user.log_33,
        user.log_34, user.log_35, user.log_36, user.log_37, user.log_38, user.log_39, user.log_40, user.log_41,
        user.log_42, user.log_43, user.log_44, user.log_45, user.log_46, user.log_47, user.log_48, user.log_49,
        user.log_50, user.log_51, user.log_52, user.log_53, user.log_54, user.log_55, user.log_56, user.log_57,
        user.log_58, user.log_59, user.log_60, user.log_61, user.log_62, user.log_63, user.log_64, user.log_65,
        user.log_66, user.log_67, user.log_68, user.log_69, user.log_70, user.log_71, user.log_72, user.log_73,
        user.log_74, user.log_75, user.log_76, user.log_77, user.log_78, user.log_79, user.log_80, user.log_81,
        user.log_82, user.log_83, user.log_84, user.log_85, user.log_86, user.log_87, user.log_88, user.log_89,
        user.log_90, user.log_91, user.log_92, user.log_93, user.log_94, user.log_95, user.log_96, user.log_97,
        user.log_98, user.log_99, user.log_100
    ]
    for log in user_logs:
        if log:
            filtred_user_logs.append(log)
    return filtred_user_logs


def create_day_goals(goal):
    """
    Алгоритм создания значения кнопок из цели пользователя

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


def change_total_goal(total_goal, login):
    """
    Смена цели пользователя
    """
    user = DayGoals.query.filter_by(login=login).first()
    user.total_goal = total_goal
    user.current_sum = 0
    db.session.commit()


def fill_day_instances(user_login):
    """
    Создание состояния кнопок в БД
    """
    # Обнуление состояния кнопок дял существующего пользователя
    if DayInstances.query.filter_by(login=user_login).first():
        user = DayInstances.query.filter_by(login=user_login).first()
        user.day_1 = None
        user.day_2 = None
        user.day_3 = None
        user.day_4 = None
        user.day_5 = None
        user.day_6 = None
        user.day_7 = None
        user.day_8 = None
        user.day_9 = None
        user.day_10 = None
        user.day_11 = None
        user.day_12 = None
        user.day_13 = None
        user.day_14 = None
        user.day_15 = None
        user.day_16 = None
        user.day_17 = None
        user.day_18 = None
        user.day_19 = None
        user.day_20 = None
        user.day_21 = None
        user.day_22 = None
        user.day_23 = None
        user.day_24 = None
        user.day_25 = None
        user.day_26 = None
        user.day_27 = None
        user.day_28 = None
        user.day_29 = None
        user.day_30 = None
        user.day_31 = None
        user.day_32 = None
        user.day_33 = None
        user.day_34 = None
        user.day_35 = None
        user.day_36 = None
        user.day_37 = None
        user.day_38 = None
        user.day_39 = None
        user.day_40 = None
        user.day_41 = None
        user.day_42 = None
        user.day_43 = None
        user.day_44 = None
        user.day_45 = None
        user.day_46 = None
        user.day_47 = None
        user.day_48 = None
        user.day_49 = None
        user.day_50 = None
        user.day_51 = None
        user.day_52 = None
        user.day_53 = None
        user.day_54 = None
        user.day_55 = None
        user.day_56 = None
        user.day_57 = None
        user.day_58 = None
        user.day_59 = None
        user.day_60 = None
        user.day_61 = None
        user.day_62 = None
        user.day_63 = None
        user.day_64 = None
        user.day_65 = None
        user.day_66 = None
        user.day_67 = None
        user.day_68 = None
        user.day_69 = None
        user.day_70 = None
        user.day_71 = None
        user.day_72 = None
        user.day_73 = None
        user.day_74 = None
        user.day_75 = None
        user.day_76 = None
        user.day_77 = None
        user.day_78 = None
        user.day_79 = None
        user.day_80 = None
        user.day_81 = None
        user.day_82 = None
        user.day_83 = None
        user.day_84 = None
        user.day_85 = None
        user.day_86 = None
        user.day_87 = None
        user.day_88 = None
        user.day_89 = None
        user.day_90 = None
        user.day_91 = None
        user.day_92 = None
        user.day_93 = None
        user.day_94 = None
        user.day_95 = None
        user.day_96 = None
        user.day_97 = None
        user.day_98 = None
        user.day_99 = None
        user.day_100 = None
        db.session.commit()
    else:
        # Создание состояния кнопок дял нового пользователя
        new_user_instances = DayInstances(login=user_login)
        db.session.add(new_user_instances)
        db.session.commit()


def fill_days_db(user_login, day_goals, goal_target):
    """
    Создание ежедневных целей пользователя
    :param user_login: Логин пользователя
    :param day_goals: Суммы для каждого дня
    :param goal_target: Общая сумма
    :return: Создание/обновление записи SQL
    """
    # Изменение ежедневных целей существующему пользователю
    if DayGoals.query.filter_by(login=user_login).first():
        user = DayGoals.query.filter_by(login=user_login).first()
        user.day_1 = day_goals[0].goal
        user.day_2 = day_goals[1].goal
        user.day_3 = day_goals[2].goal
        user.day_4 = day_goals[3].goal
        user.day_5 = day_goals[4].goal
        user.day_6 = day_goals[5].goal
        user.day_7 = day_goals[6].goal
        user.day_8 = day_goals[7].goal
        user.day_9 = day_goals[8].goal
        user.day_10 = day_goals[9].goal
        user.day_11 = day_goals[10].goal
        user.day_12 = day_goals[11].goal
        user.day_13 = day_goals[12].goal
        user.day_14 = day_goals[13].goal
        user.day_15 = day_goals[14].goal
        user.day_16 = day_goals[15].goal
        user.day_17 = day_goals[16].goal
        user.day_18 = day_goals[17].goal
        user.day_19 = day_goals[18].goal
        user.day_20 = day_goals[19].goal
        user.day_21 = day_goals[20].goal
        user.day_22 = day_goals[21].goal
        user.day_23 = day_goals[22].goal
        user.day_24 = day_goals[23].goal
        user.day_25 = day_goals[24].goal
        user.day_26 = day_goals[25].goal
        user.day_27 = day_goals[26].goal
        user.day_28 = day_goals[27].goal
        user.day_29 = day_goals[28].goal
        user.day_30 = day_goals[29].goal
        user.day_31 = day_goals[30].goal
        user.day_32 = day_goals[31].goal
        user.day_33 = day_goals[32].goal
        user.day_34 = day_goals[33].goal
        user.day_35 = day_goals[34].goal
        user.day_36 = day_goals[35].goal
        user.day_37 = day_goals[36].goal
        user.day_38 = day_goals[37].goal
        user.day_39 = day_goals[38].goal
        user.day_40 = day_goals[39].goal
        user.day_41 = day_goals[40].goal
        user.day_42 = day_goals[41].goal
        user.day_43 = day_goals[42].goal
        user.day_44 = day_goals[43].goal
        user.day_45 = day_goals[44].goal
        user.day_46 = day_goals[45].goal
        user.day_47 = day_goals[46].goal
        user.day_48 = day_goals[47].goal
        user.day_49 = day_goals[48].goal
        user.day_50 = day_goals[49].goal
        user.day_51 = day_goals[50].goal
        user.day_52 = day_goals[51].goal
        user.day_53 = day_goals[52].goal
        user.day_54 = day_goals[53].goal
        user.day_55 = day_goals[54].goal
        user.day_56 = day_goals[55].goal
        user.day_57 = day_goals[56].goal
        user.day_58 = day_goals[57].goal
        user.day_59 = day_goals[58].goal
        user.day_60 = day_goals[59].goal
        user.day_61 = day_goals[60].goal
        user.day_62 = day_goals[61].goal
        user.day_63 = day_goals[62].goal
        user.day_64 = day_goals[63].goal
        user.day_65 = day_goals[64].goal
        user.day_66 = day_goals[65].goal
        user.day_67 = day_goals[66].goal
        user.day_68 = day_goals[67].goal
        user.day_69 = day_goals[68].goal
        user.day_70 = day_goals[69].goal
        user.day_71 = day_goals[70].goal
        user.day_72 = day_goals[71].goal
        user.day_73 = day_goals[72].goal
        user.day_74 = day_goals[73].goal
        user.day_75 = day_goals[74].goal
        user.day_76 = day_goals[75].goal
        user.day_77 = day_goals[76].goal
        user.day_78 = day_goals[77].goal
        user.day_79 = day_goals[78].goal
        user.day_80 = day_goals[79].goal
        user.day_81 = day_goals[80].goal
        user.day_82 = day_goals[81].goal
        user.day_83 = day_goals[82].goal
        user.day_84 = day_goals[83].goal
        user.day_85 = day_goals[84].goal
        user.day_86 = day_goals[85].goal
        user.day_87 = day_goals[86].goal
        user.day_88 = day_goals[87].goal
        user.day_89 = day_goals[88].goal
        user.day_90 = day_goals[89].goal
        user.day_91 = day_goals[90].goal
        user.day_92 = day_goals[91].goal
        user.day_93 = day_goals[92].goal
        user.day_94 = day_goals[93].goal
        user.day_95 = day_goals[94].goal
        user.day_96 = day_goals[95].goal
        user.day_97 = day_goals[96].goal
        user.day_98 = day_goals[97].goal
        user.day_99 = day_goals[98].goal
        user.day_100 = day_goals[99].goal
        db.session.commit()
    else:
        # Создание ежедневных целей новому пользователю
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


def update_current_sum(login):
    current_sum = 0
    user = DayInstances.query.filter_by(login=login).first()
    days = [
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
    for day in days:
        if day:
            current_sum += day
    user = DayGoals.query.filter_by(login=login).first()
    user.current_sum = current_sum


@login_manager.user_loader
def load_user(user_id):
    return UserAuth.query.get(user_id)

