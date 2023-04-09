"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
import datetime
from app.models import Movies
from app.forms import MovieForm
import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/movies', methods=['POST'])
def movies():
    
    if request.method == "POST":
        form =MovieForm()

        if form.validate_on_submit():
            poster = form.poster.data
            postername = secure_filename(poster.filename)
            title = form.title.data
            description = form.description.data
            created_at = datetime.datetime.now()

            if poster and (postername != "" and postername != " "):
                poster.save(os.path.join(app.config['UPLOAD_FOLDER'], postername))

                newmovie = Movies((title, description, postername, created_at))
                db.session.add(newmovie)
                db.session.commit()
                
                response= {
                    "message": "Movie Successfully added",
                    "title": title,
                    "poster": postername,
                    "description": description
                }
                return jsonify(response)
        ferrors ={"errors": form_errors(form) }  
        return jsonify(ferrors)
    
    return jsonify({'message': 'This is not an accepted request'})



###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

