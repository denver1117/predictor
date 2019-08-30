"""
Test flask app
"""

import flask 

from predictor import predict

def test_request_method():
    with predict.app.test_request_context('/?method=predict'):
        assert flask.request.path == '/'
        assert flask.request.args['method'] == 'predict'

def test_request_features():
    with predict.app.test_request_context('/?feature1=5'):
        assert flask.request.path == '/'
        assert flask.request.args['feature1'] == '5'

def test_get():
    with predict.app.test_client() as c:
        rv = c.get('/?method=predict_proba')
        assert flask.request.args['method'] == 'predict_proba'
