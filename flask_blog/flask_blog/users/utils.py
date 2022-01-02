import os
import secrets
from PIL import Image

from flask_blog import mail
from flask_blog import app
from flask_mail import Message


def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message("Password Reset Request", sender="mohsinashraf121102@gmail.com", recipients=[user.email])
	msg.body = f"""To reset your password, visit the following link.
{url_for('reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email, and not changes will be made.
"""
	mail.send(msg)



def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	profile_filename = random_hex + f_ext
	picture_path = os.path.join(app.root_path, "static/profile_pics", profile_filename)
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return profile_filename

