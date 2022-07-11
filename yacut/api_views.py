from http import HTTPStatus
from urllib.parse import urljoin

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .views import get_unique_short_id, letters_and_digits


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if ('custom_id' not in data
            or data['custom_id'] is None
            or data['custom_id'] == ''):
        data['custom_id'] = get_unique_short_id()
    short_id = str(data['custom_id'])
    if (not all(x in letters_and_digits for x in short_id)
            or len(data['custom_id']) > 16):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URL_map.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
    url_map = URL_map()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    dict_url = url_map.to_dict()
    short_path = urljoin(request.url_root, data['custom_id'])
    return (
        jsonify({'url': dict_url['url'], 'short_link': short_path}),
        HTTPStatus.CREATED
    )


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_opinion(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    dict_url = url_map.to_dict()
    return jsonify({'url': dict_url['url']}), HTTPStatus.OK
