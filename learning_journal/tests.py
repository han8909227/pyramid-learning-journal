"""Testing for pyramid server."""
from pyramid.testing import DummyRequest
from pyramid.response import Response
from learning_journal.views.default import list_view, detail_view, create_view, update_view


def test_list_view_return_response_obj():
    """Assert if the request returns a valid response."""
    req = DummyRequest()
    response = list_view(req)
    assert isinstance(response, Response)


def test_list_view_return_200():
    """Assert if the response code is 200."""
    req = DummyRequest()
    response = list_view(req)
    assert response.status_code == 200


def test_list_view_content():
    """Assert the content for response contains corresponding body."""
    req = DummyRequest()
    response = list_view(req)
    assert 'Home Page' in response.body


def test_detail_view_return_response_obj():
    """Assert if the request returns a valid response."""
    req = DummyRequest()
    response = detail_view(req)
    assert isinstance(response, Response)


def test_detial_view_return_200():
    """Assert if the response code is 200."""
    req = DummyRequest()
    response = detail_view(req)
    assert response.status_code == 200


def test_detail_view_content():
    """."""
    req = DummyRequest()
    response = detail_view(req)
    assert 'View single entry' in response.ubody


def test_create_view_return_response_obj():
    """Assert if the request returns a valid response."""
    req = DummyRequest()
    response = create_view(req)
    assert isinstance(response, Response)


def test_create_view__return_200():
    """Assert if the response code is 200."""
    req = DummyRequest()
    response = create_view(req)
    assert response.status_code == 200


def test_create_view_content():
    """."""
    req = DummyRequest()
    response = create_view(req)
    assert 'Creating a New Entry' in response.ubody


def test_update_view_return_response_obj():
    """Assert if the request returns a valid response."""
    req = DummyRequest()
    response = update_view(req)
    assert isinstance(response, Response)


def test_update_view__return_200():
    """Assert if the response code is 200."""
    req = DummyRequest()
    response = update_view(req)
    assert response.status_code == 200


def test_update_view_content():
    """."""
    req = DummyRequest()
    response = update_view(req)
    assert 'Edit an entry' in response.ubody
