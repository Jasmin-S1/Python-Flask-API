from lista import app
from flask import render_template, redirect, url_for, flash, request
from lista.models import Doctor
from lista.forms import LoginForm, RegisterForm
from lista import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def start_page():
    return render_template('base.html')


@app.route('/login', methods=['GET'])
def login_page():
    form = LoginForm()
    # if form.validate_on_submit():
    #     attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
    #     if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
    #         login_user(attempted_user)
    #         flash(f'Success! You are logged in as: {attempted_user.email_address}', category='success')
    #         return redirect(url_for('home_page'))
    #     else:
    #         flash('Email address and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        doctor_to_create = Doctor(
                              email_address=form.email_address.data,
                              password=form.password.data)
        db.session.add(doctor_to_create)
        db.session.commit()
        
        login_user(doctor_to_create)
        flash(f'Account created successfully! You are now logged in as {doctor_to_create.email_address}', category='success')

        return redirect(url_for('patients_page'))
    if form.errors != {}:  # IF THERE ARE NOT ERRORS FROM THE VALIDATIONS (form.errors is dictionary)
        for err_msg in form.errors.values():
            flash(f'There was a problem with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/patients')
@login_required
def patients_page():
    return render_template('patients.html')
