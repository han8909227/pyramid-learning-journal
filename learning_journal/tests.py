"""Testing for pyramid server."""
from pyramid.testing import DummyRequest
from pyramid.response import Response
from learning_journal.views.default import list_view, detail_view, create_view, update_view


def test_list_view_return_response_obj():
    """."""
    req = DummyRequest()
    response = list_view(req)
    assert isinstance(response, Response)


def test_return_200():
    """."""
    req = DummyRequest()
    response = list_view(req)
    assert response.status_code == 200


def test_content():
    """."""
    req = DummyRequest()
    response = list_view(req)
    with open('learning_journal/templates/HB-mockups/index.html', 'r') as fn:
        assert response == Response(fn.read())
