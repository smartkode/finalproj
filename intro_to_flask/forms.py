from flask_wtf import Form
from wtforms import TextField, FileField, PasswordField, TextAreaField, DateTimeField, SubmitField, IntegerField, SelectField, validators, ValidationError
from models import db, Officer
 
class ContactForm(Form):
	name = TextField("Name", [validators.Required("Please enter your name.")])
	email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	subject = TextField("Subject", [validators.Required("Please enter a subject.")])
	message = TextAreaField("Message", [validators.Required("Please enter a message.")])
	submit = SubmitField("Send")

class LoginForm(Form):
	name = TextField("Name", [validators.Required("Please enter your name.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	submit = SubmitField("Login")

class SignupForm(Form):
	firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
	lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
	email_address = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	submit = SubmitField("Create Profile")

 
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
	  		return False
	 
		user = Officer.query.filter_by(email_address = self.email_address.data.lower()).first()
		if user:
	  		self.email.errors.append("That email is already taken")
	  		return False
		else:
	  		return True

class ProfileForm(Form):
	picture = FileField("Photo")
	gender = SelectField(u'Gender', choices=[('select', "Select"), ('female', "Female"), ('male', "Male")])
	first_name = TextField("First Name", [validators.Required("Please enter your name.")])
	middle_name = TextField("Middle Name")
	last_name = TextField("Last Name")
	weapon_of_choice = TextField("Weapon Of Choice")
	height = TextField("Height")
	weight = TextField("Weight")
	build = TextField("Build")
	complexion = TextField("Complexion")
	hair_colour = TextField("Hair Colour")
	eye_colour = TextField("Eye Colour")
	ethnicity = TextField("Ethnicity")
	scars = TextField("Scars")
	work_address = TextAreaField("Work Address")
	work_contact_no = TextField("Work Contact Number")
	job_title = TextField("Job Title")
	mother_first_name = TextField("Mother's First Name")
	mother_maiden_name = TextField("Mother's Maiden Name")
	mother_surname = TextField("Mother's Surname")
	mother_address = TextAreaField("Mother's Address")
	mother_nationality = TextField("Mother's Nationality")
	father_first_name = TextField("Father's First Name")
	father_surname = TextField("Father's Surname")
	father_address = TextAreaField("Father's Address")
	father_nationality = TextField("Father's Nationality")
	submit = SubmitField("Submit")

class ReportForm(Form):
	status = TextField("Status")
	diary_entry_number = IntegerField("Diary Entry Number")
	location_of_offence = TextAreaField("Location of Offence")
	significant_landmark_nearby = TextField("Significant Landmark Nearby")
	offence = TextField("Offence")
	offence_code = IntegerField("Offence Code")
	reported_date_and_time = DateTimeField("Reported Date & Time")
	name_of_victim = TextField("Name of Victim")
	address_of_victim = TextAreaField("Address of Victim")
	age_of_victim = IntegerField("Age of Victim")
	height_of_victim = TextField("Height of Victim")
	ethnicity_of_victim = TextField("Ethnicity of Victim")
	weapon_used = TextField("Weapon Used")
	submit = SubmitField("Submit")

