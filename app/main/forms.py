from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError, BooleanField, TextAreaField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

#Pitch Form
class PitchForm(FlaskForm):
    category_id = SelectField('Pick A Category', choices=[('1', 'Sales'), ('2', 'Product'), ('3', 'Secrets'), ('4', ('Confessions'), ('5', 'Reviews'))])
    comment = TextAreaField('Comments')
    submit = SubmitField('Submit Commennt')

#Comment Form
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])

#categoryForm
class CategoryForm(FlaskForm):
    name = StringField('Pitch', validators=[Required()])
    title = TextAreaField('Pitch')
    submit = SubmitField()