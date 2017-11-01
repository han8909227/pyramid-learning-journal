"""Testing for pyramid server."""
from pyramid.testing import DummyRequest
from learning_journal.data.list_journal import Journals
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.views.default import list_view, detail_view, create_view, update_view


def test_list_view_return_response_obj():
    """Assert if the index request returns a valid response."""
    req = DummyRequest()
    response = list_view(req)
    assert response['journal'] == Journals


def test_detail_view_response():
    """Assert if the detail view request returns a valid response."""
    req = DummyRequest()
    for num in range(10):
        req.matchdict['id'] = num + 1
        response = detail_view(req)
        assert response['Journal'] == Journals[num]


def test_detail_view_error():
    """."""
    req = DummyRequest()
    req.matchdict['id'] = 100
    try:
        detail_view(req)
    except HTTPNotFound:
        pass


def test_create_view_response():
    """Assert if the create view request returns a valid response."""
    req = DummyRequest()
    response = create_view(req)
    assert response['for_test'] == 'for_test'


def test_update_view_response():
    """Assert if the request returns a valid response."""
    req = DummyRequest()
    response = update_view(req)
    assert response['for_test'] == 'for_test'

