"""
https://github.com/CalebCurry/flask-notes
https://github.com/CalebCurry/testimionials
"""
from testimonials import app
from flask import render_template, abort

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
def page_not_forund(e):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/testimonials')
def index():
    return render_template('index.html', testimonials=testimonial_list)


@app.route('/testimonials/<id>')
def get_testimonial(id):
    for testimonial in testimonial_list:
        if testimonial.get('id') == int(id):
            return render_template('testimonial.html', testimonial=testimonial)
        abort(404)
        
# @app.route('/api/testimonials')
# def testimonials():
#     return {'testimonails': ['great', 'its ok', 'fantastic', 'noice']}
