from flask import Flask, Response
from flask import request
from flask_cachecontrol import (
    FlaskCacheControl,
    cache,
    cache_for,
    dont_cache
)

flask_cache_control = FlaskCacheControl()


app = Flask(__name__)
flask_cache_control.init_app(app)


@app.route('/')
@cache_for(seconds=10)
def index():
    return 'index'


@app.route('/expires')
def expires():
    return 'expires'


@app.route('/cache-control/public')
# @cache(max_age=10, public=True)
def public():
    response = Response('public')
    response.headers['Cache-Control'] = 'max-age=10,public'
    return response


@app.route('/cache-control/private')
# @cache(max_age=10, private=True)
def private():
    response = Response('private')
    response.headers['Cache-Control'] = 'max-age=10,private'
    return response


@app.route('/cache-control/max-age')
# @cache_for(seconds=10)
def max_age():
    max_age = request.args.get('max-age', 10)
    response = Response('max-age')
    # response.headers['Cache-Control'] = 'max-age=10'
    response.cache_control.max_age = max_age
    return response


@app.route('/cache-control/min-fresh')
# @cache(min_fresh=10)
def min_fresh():
    response = Response('min-fresh')
    response.headers['Cache-Control'] = 'min-fresh=10'
    # response.cache_control.min_fresh = 10
    return response


@app.route('/cache-control/no-cache')
def no_cache():
    response = Response('no-cache')
    # response.headers['Cache-Control'] = 'no-cache'
    response.cache_control = 'no-cache'
    return response


@app.route('/cache-control/no-store')
def no_store():
    response = Response('no-store')
    # response.headers['Cache-Control'] = 'no-store'
    response.cache_control = 'no-store'
    return response


if __name__ == "__main__":
    app.run(debug=True)
