from lista import bcrypt
from flask_login import UserMixin
from lista import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return Doctor.query.get(int(user_id))


class Doctor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=50), nullable=False)
    assigned_patient = db.relationship('Patient', backref='patients')

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)    



class Patient(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    symptoms = db.Column(db.String, nullable=False)
    assigned_doctor = db.Column(db.Integer, db.ForeignKey('doctor.id'))

db.create_all()