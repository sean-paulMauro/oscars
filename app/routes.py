from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, SubmitCategoryForm, SubmitNomineeForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import AppUser, CategoryLookup, NomineeLookup
from werkzeug.urls import url_parse
from datetime import datetime


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        app_user = AppUser.query.filter_by(email=form.email.data).first()
        if app_user is None or not app_user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(app_user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # noinspection PyArgumentList
        app_user = AppUser(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
        app_user.set_password(form.password.data)
        db.session.add(app_user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user')
@app.route('/user/<int:user_id>')
@login_required
def user(user_id=None):
    if user_id is None:
        return render_template('user.html', user=current_user)
    else:
        return render_template('user.html', user=AppUser.query.filter_by(id=user_id).first_or_404())


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)


@app.route('/categories', methods=['GET', 'POST'])
@login_required
def categories():
    if request.method == "POST":
        if request.form.get('add_category') == "Add a Category":
            return redirect(url_for('submit_category'))
    rows = CategoryLookup.query.all()
    return render_template('categories.html', title='Categories', rows=rows)


@app.route('/submit_category', methods=['GET', 'POST'])
def submit_category():
    form = SubmitCategoryForm()
    if form.validate_on_submit():
        category = CategoryLookup(name=form.category.data,
                                  points=form.points.data, notes=form.notes.data)
        db.session.add(category)
        db.session.commit()
        flash('Category added!')
        return redirect(url_for('categories'))
    return render_template('submit_category.html', title='Submit category', form=form)


@app.route('/nominees', methods=['GET', 'POST'])
@login_required
def nominees():
    if request.method == "POST":
        if request.form.get('add_nominee') == "Add a Nominee":
            return redirect(url_for('submit_nominee'))
    rows = NomineeLookup.query.all()
    return render_template('nominees.html', title='Nominees', rows=rows)


@app.route('/submit_nominee', methods=['GET', 'POST'])
def submit_nominee():
    form = SubmitNomineeForm()
    if form.validate_on_submit():
        nominee = NomineeLookup(name=form.nominee.data,
                                points=form.year.data)
        db.session.add(nominee)
        db.session.commit()
        flash('Nominee added!')
        return redirect(url_for('nominees'))
    return render_template('submit_nominee.html', title='Submit nominee', form=form)
