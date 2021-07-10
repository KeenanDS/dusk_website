#story/views.py
from flask import render_template,url_for,flash,request,redirect,Blueprint
from flask_login import current_user ,login_required
from dusk import db
from dusk.models import Story
from dusk.story.forms import StoryForm

storys = Blueprint('storys',__name__)


#CREATE
@storys.route('/create',methods=['GET','POST'])
@login_required
def create_story():
    form = StoryForm()

    if form.validate_on_submit():

        story = Story(title=form.title.data,
                    text=form.text.data,
                    user_id=current_user.id,
                    )

        db.session.add(story)
        db.session.commit()
        flash('Story Saved')
        return redirect(url_for('core.index'))

    return render_template('create_story.html',form=form)



#STORY VIEW
@storys.route('/<int:story_id>')
def story(story_id):
    story = Story.query.get_or_404(story_id)
    return render_template('story.html',title=story.title,
                            date=story.date,post=story)



#UPDATE
@storys.route('/<int:story_id>/update',methods=['GET','POST'])
@login_required
def update(story_id):
    story = Story.query.get_or_404(story_id)

    if story.author != current_user:
        abort(403)

    form = StoryForm

    if form.validate_on_submit():

        story.title = form.title.data
        story.text = form.text.data
        db.session.commit()
        flash('Story Updated')
        return redirect(url_for('storys.story',story_id=story.id))

    elif request.method == 'GET': #Potential Error###################################################
        form.title.data = story.title
        form.text.data = story.text

    return render_template('create_story.html',title='Updating',form=form)


#DELETE
@storys.route('/<int:story_id>/delete',methods=['GET','POST'])
@login_required
def delete_story(story_id):

    story = Story.query.get_or_404(story_id)

    if story.author != current_user:
        abort(403)
    
    db.session.delete(story)
    db.session.commit()
    return redirect(url_for('core.index'))
