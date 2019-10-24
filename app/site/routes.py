from flask import render_template

from . import site_bp
from app.models import TableName


@site_bp.route('/', methods=['GET'])
def index():
    records = TableName.query.all()
    return render_template('index.html', records=records)
