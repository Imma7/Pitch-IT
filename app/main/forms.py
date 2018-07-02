from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError, BooleanField, TextAreaField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category_id = SelectField('Pick A Category', choices=[('1', 'Sales'), ('2', 'Product'), ('3', 'Secrets'), ('4', ('Confessions'), ('5', 'Reviews'))])
    comment = TextAreaField('Comments')
    submit = SubmitField('Submit Commennt')