"""
Test imports
"""

try:
    from predictor import *
    _top_import_error = None
except Exception as e:
    _top_import_error = e

try:
    from predictor import predict
    _module_import_error = None
except Exception as e:
    _module_import_error = e

try:
    import predictor
    _package_import_error = None
except Exception as e:
    _package_import_error = e

def test_import_predict():
    assert _top_import_error == None

def test_import_module():
    assert _module_import_error == None

def test_import_package():
    assert _package_import_error == None

