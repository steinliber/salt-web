# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import login_required

blueprint = Blueprint('minion', __name__,
                      url_prefix='/minions', static_folder='../static')


@blueprint.route('/')
@login_required
def status():
    return render_template('minion/status.html')
