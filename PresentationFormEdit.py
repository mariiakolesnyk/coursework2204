from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, HiddenField
from wtforms import validators


class PresentationFormEdit(FlaskForm):
    presentation_name = HiddenField("Name: ", [validators.Length(2, 40, "Name should be from 2 to 40 symbols")])
    presentation_date = DateField("Date: ")
    presentation_link = DateField("Link: ",
                                  # validators.DataRequired("Please enter name of presentation."),
                                  validators.Length(5, 500, "Link should be from 2 to 40 symbols")
                                  )

    submit = SubmitField("Save")