import os
import secrets

from flask import current_app, url_for
from flask_mail import Message
from PIL import Image
from zuman import mail, constants


def save_picture(form_picture):
    rand_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    pic_fn = rand_hex + f_ext
    pic_path = os.path.join(current_app.root_path, 'static/profile_pics', pic_fn)

    out_size = (300, 300)
    i = Image.open(form_picture)
    w, h = i.size
    a = w if w <= h else h
    left = (w - a) / 2
    top = (h - a) / 2
    right = (w + a) / 2
    bottom = (h + a) / 2
    img = i.crop((left, top, right, bottom))
    img = img.resize(out_size)
    img.save(pic_path)

    return pic_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        'Password Reset Request',
        sender=f"noreply@{os.getenv('SERVER_NAME')}",
        recipients=[user.email])
    if os.getenv('FLASK_APP') == constants.FLASK_APP_DEV:
        url = url_for('users.reset_token', token=token, _external=True)
    else:
        protocol = "https" if os.getenv('SESSION_COOKIE_SECURE') == "True" else "http"
        url = f"{protocol}://{os.getenv('SERVER_NAME')}{url_for('users.reset_token', token=token)}"
    msg.body = f'''To reset your password, visit:
        {url}
        Ignore if not requested by you.'''
    mail.send(msg)
