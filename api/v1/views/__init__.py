#!/usr/bin/python3
"""Flask app"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if __name__ == '__main__':
    if app_views:
        from api.v1.views.index import *
        # from api.v1.views.states import *
        # from api.v1.views.cities import *
        # from api.v1.views.amenities import *
        # from api.v1.views.users import *
        # from api.v1.views.places import *
        # from api.v1.views.places_reviews import *
        # from api.v1.views.places_amenities import *
