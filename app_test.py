# app_test.py
from streamlit.testing.v1 import AppTest

def test_app_runs():
    """Test that the Streamlit app launches without error."""
    at = AppTest.from_file("app.py")
    at.run()
    assert not at.exception

def test_app_title():
    """Example basic test: Check if app contains a title."""
    at = AppTest.from_file("app.py")
    at.run()
    assert any(getattr(el, "tag", "") == "st.title" for el in at.elements)
