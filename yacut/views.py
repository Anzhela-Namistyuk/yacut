import random
from http import HTTPStatus

from flask import flash, redirect, render_template

from . import app, db
from .forms import URL_mapForm, letters_and_digits
from .models import URL_map


def get_unique_short_id():
    short_link = ''.join(random.sample(letters_and_digits, 6))
    return short_link


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        if URL_map.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            return render_template('url_map.html', form=form)
        url_map = URL_map(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(url_map)
        db.session.commit()
        context = {'short_id': custom_id, 'form': form}
        return render_template('url_map.html', **context), HTTPStatus.OK
    return render_template('url_map.html', form=form)


@app.route('/<string:short_id>')
def get_original_link(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first_or_404()
    if url_map:
        return redirect(url_map.original)
