from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from backend import db
from flask_login import UserMixin


class UserModel(db.Model, UserMixin):

    __tablename__ = 'user_table'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # must have username, passoword and uoft_email
    username = db.Column(db.String(20), unique=True, nullable=False)
    uoft_email = db.Column(db.String(50), unique=True, nullable=False)
    # the orginaztion table is not ready rn, need to add
    # supplementary information needed
    # store student_id as a string, as the passed in data from frontend would be string
    uoft_student_id = db.Column(db.String(20))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    department = db.Column(db.String(50))
    enrolled_time = db.Column(db.String(20))
    # authorziation check used column
    authenticated = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # columns used for post events, check hosts
    organizational_role = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the user id"""
        return self.user_id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def is_host(self):
        """Return True if the user is a host."""
        return self.organizational_role

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @property
    def formatted_enrolled_time(self):
        if self.enrolled_time:
            enrolled_time_datetime = datetime.strptime(
                self.enrolled_time, "%m/%Y")
            return enrolled_time_datetime.strftime("%m/%Y")
        else:
            return None

    @password.setter
    def password(self, password):
        from backend import bcrypt  # noqa
        self.password_hash = bcrypt.generate_password_hash(password)

    def verify_password(self, password):
        from backend import bcrypt  # noqa
        return bcrypt.check_password_hash(self.password_hash, password)

    def __init__(self, username=None, password_hash=None, uoft_email=None,
                 uoft_student_id=None, first_name=None, last_name=None,
                 department=None, authenticated=False,
                 organizational_role=False, enrolled_time=None):
        self.username = username
        self.password_hash = password_hash
        self.uoft_email = uoft_email
        self.uoft_student_id = uoft_student_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.enrolled_time = enrolled_time
        self.authenticated = authenticated
        self.organizational_role = organizational_role