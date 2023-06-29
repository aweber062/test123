import dash
from dash.testing.application_runners import import_app
from dash.testing.browser import Browser

def test_header_presence():
    app = import_app("my_app.py")
    runner = Browser(app)
    runner.wait_for_element("#header")

def test_visualization_presence():
    app = import_app("my_app.py")
    runner = Browser(app)
    runner.wait_for_element("#visualization")

def test_region_picker_presence():
    app = import_app("my_app.py")
    runner = Browser(app)
    runner.wait_for_element("#region-picker")
