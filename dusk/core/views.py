# core/views.py
from dusk.models import Story
from flask import render_template, request, Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    story = Story.query.order_by(Story.date.desc()).paginate(page=page,per_page=5)
    return render_template('index.html',story=story)


@core.route('/info')
def info():
    return render_template('info.html')