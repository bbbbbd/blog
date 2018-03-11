# -*- coding: utf-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__)
from . import views, errors, forms
from ..modes import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
