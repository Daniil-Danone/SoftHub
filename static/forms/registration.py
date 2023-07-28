from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired


class RegForm(FlaskForm):
    email = EmailField('Почта',
                       validators=[DataRequired(message='Это поле обязательно!')],
                       name='login',
                       id='email',
                       render_kw={
                           'placeholder': "Please, enter the correct email",
                       }
                       )
    password = StringField('Пароль',
                           validators=[DataRequired(message='Это поле обязательно!')],
                           name='password',
                           id='password',
                           render_kw={
                               'placeholder': "Please, provide a password"
                           }
                           )

