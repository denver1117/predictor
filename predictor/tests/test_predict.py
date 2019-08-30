"""
Test imports
"""

try:
    from predictor import predict
    _top_import_error = None
except Exception as e:
    _top_import_error = e

def test_import_predict():
    assert _top_import_error == None


