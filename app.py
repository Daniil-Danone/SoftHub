import os
import datetime
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_user, current_user, logout_user
from static.forms.registration import RegForm
from static.forms.login import LoginForm
from static.forms.profile import ProfileForm
from static.data.users import User
from static.data import db_session
from geopy.geocoders import Nominatim


load_dotenv(find_dotenv())

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/', methods=['POST', 'GET'])
def index():
    db_session.global_init("softhub.db")
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)

    form = LoginForm()

    if current_user.is_authenticated:
        return render_template('index.html',
                               title='SoftHUB | Проект о том, как развить SoftSkills',
                               user=current_user,
                               ip_addr=ip_addr)

    else:
        if form.validate_on_submit():
            print('ok')
            db_sess = db_session.create_session()
            user = db_sess.query(User).filter(User.email == form.email.data).first()
            print(form.email.data, form.password.data)
            if user:
                if user.check_password(form.password.data):
                    login_user(user)
                    return redirect('/')
                return render_template('index.html',
                                       form=form,
                                       error='Неверный пароль!',
                                       title='SoftHUB | Авторизация')
            return render_template('index.html',
                                   form=form,
                                   error='Аккаунта с таким логином не существует!',
                                   title='SoftHUB | Авторизация')
        return render_template('index.html',
                               form=form,
                               title='SoftHUB | Проект о том, как развить SoftSkills')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    reg_form = RegForm()
    user = User()
    if reg_form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == reg_form.email.data).first():
            return render_template('registration.html',
                                   title='SoftHUB | Регистрация',
                                   reg_form=reg_form,
                                   email_error=f'Почта -- {reg_form.email.data} -- занята!')
        else:
            user.email = reg_form.email.data
            user.set_password(reg_form.password.data)
            user.created_date = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S')

            db_sess.add(user)
            db_sess.commit()
            return redirect('/')
    return render_template('registration.html',
                           title='Регистрация',
                           reg_form=reg_form)


@app.route('/profile/<int:id>', methods=['POST', 'GET'])
def profile(id):
    profile_form = ProfileForm()
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id).first()
    if request.method == 'GET':
        if user:
            profile_form.email.data = user.email
            profile_form.name.data = user.name
            profile_form.surname.data = user.surname
            profile_form.age.data = user.age
            profile_form.nickname.data = user.nickname
            profile_form.status.data = user.status
            profile_form.sex.data = user.sex
            profile_form.about_me.data = user.about_me
            profile_form.skills.data = user.skills
            profile_form.address.data = user.address

    if current_user.is_authenticated:
        if profile_form.validate_on_submit():
            if user:
                user.name = profile_form.name.data
                user.surname = profile_form.surname.data
                user.age = profile_form.age.data
                user.sex = profile_form.sex.data
                user.status = profile_form.status.data
                user.address = profile_form.address.data
                geolocator = Nominatim(user_agent="SoftHUB")
                location = geolocator.geocode(user.address)
                user.latitude = location.latitude
                user.longitude = location.longitude

                if profile_form.avatar.data is not None:
                    img = profile_form.avatar.data
                    img.save(f"static/img/avatars/{current_user.email}.png")
                    user.avatar_path = f"/img/avatars/{current_user.email}.png"
                db_sess.commit()
                return redirect(f'/profile/{current_user.id}')

    else:
        return redirect('/registration')

    return render_template('profile.html',
                           title=f'Профиль | {user.nickname}',
                           user=user,
                           profile_form=profile_form)


@app.route('/map', methods=['POST', 'GET'])
def map():
    form = LoginForm()
    db_sess = db_session.create_session()
    people = db_sess.query(User).all()

    if current_user.is_authenticated:
        user = current_user
        return render_template('map.html',
                               title=f'Интерактивная карта',
                               people=people,
                               user=user)
    return render_template('map.html',
                           title=f'Интерактивная карта',
                           people=people,
                           form=form)


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run()
