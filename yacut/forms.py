import string

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, ValidationError


letters_and_digits = (string.ascii_letters +
                      string.digits + string.ascii_uppercase)


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 256)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, 16), Optional()])
    submit = SubmitField('Создать')

    def validate_custom_id(self, custom_id):
        short_id = str(self.custom_id.data)
        if not all(x in letters_and_digits for x in short_id):
            raise ValidationError('Указано недопустимое имя  для короткой ссылки')
