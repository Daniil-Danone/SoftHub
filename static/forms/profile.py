from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class ProfileForm(FlaskForm):
    email = EmailField('Почта',
                       validators=[DataRequired(message='Это поле обязательно!')],
                       name='email',
                       id='email',
                       render_kw={
                           'placeholder': "Почта"
                       })
    name = StringField('Имя',
                       name='name',
                       id='name',
                       render_kw={
                           'placeholder': "Имя"
                       })
    surname = StringField('Фамилия',
                          name='surname',
                          id='surname',
                          render_kw={
                           'placeholder': "Фамилия"
                          })
    age = StringField('Возраст',
                      name='age',
                      id='age',
                      render_kw={
                          'placeholder': "Возраст"
                      })
    nickname = StringField('Никнейм',
                           name='nickname',
                           id='nickname',
                           render_kw={
                               'placeholder': "Никнейм"
                           })

    address = StringField('Адрес',
                          name='address',
                          id='address',
                          render_kw={
                              'placeholder': "Адрес"
                          })
    status = StringField('Статус',
                         name='status',
                         id='status',
                         render_kw={
                             'placeholder': "Статус"
                         })
    sex = StringField('Пол',
                      name='sex',
                      id='sex',
                      render_kw={
                          'placeholder': "Пол"
                      })
    about_me = TextAreaField('О себе',
                             name='about_me',
                             id='about_me',
                             render_kw={
                                 'placeholder': "О себе"
                             })
    avatar = FileField('Контент', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])

    skills = StringField('SoftSkills',
                         name='skills',
                         id='skills',
                         render_kw={
                             'placeholder': "SoftSkills"
                         })

