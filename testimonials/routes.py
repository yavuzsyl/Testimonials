"""
https://github.com/CalebCurry/flask-notes
https://github.com/CalebCurry/testimionials
"""
from turtle import title
from testimonials import app, db
from flask import render_template, abort, jsonify, request
from testimonials.models import Testimonial

testimonial_list = [
    {
        'id': 10,
        'name': 'Connor1',
        'message': 'nice'
    },
    {
        'id': 11,
        'name': 'Connor2',
        'message': 'nice'
    },
    {
        'id': 12,
        'name': 'Connor3',
        'message': 'nice'
    },
    {
        'id': 13,
        'name': 'Connor4',
        'message': 'nice'
    }
]


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
@app.route('/testimonials')
def index():
    return render_template('index.html', testimonials=testimonial_list)


@app.route('/api/testimonials/<id>')
def get_testimonial_id(id):
    testimonial = Testimonial.query.get(id)
    if testimonial:
        return jsonify(testimonial)

    return {}


@app.route('/testimonials/<id>')
def get_testimonial(id):
    for testimonial in testimonial_list:
        if testimonial.get('id') == int(id):
            return render_template('testimonial.html', testimonial=testimonial)
        abort(404)


@app.route('/api/testimonials')
def get_testimonials():
    testimonials = Testimonial.query.all()
    return jsonify({'testimonials': testimonials})


@app.route('/api/testimonials', methods=['POST'])
def add_testimonial():
    data = request.get_json()
    testimonial = Testimonial(name=data.get('name'), testimonial=data.get('testimonial'))
    db.session.add(testimonial)
    db.session.commit()
    return testimonial.id
