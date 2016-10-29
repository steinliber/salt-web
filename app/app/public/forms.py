# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms.validators import DataRequired

from app.user.models import User


class LoginForm(Form):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(username=self.username.data).first()
        print(self.username.data, self.user)
        if not self.user:
            self.username.errors.append('用户名不存在')
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append('密码无效')
            return False

        if not self.user.active:
            self.username.errors.append('用户还未激活')
            return False
        return True
