"""Default."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.models import MyModel


@view_config(route_name='list_view', renderer='learning_journal:templates/HB-mockups/index.jinja2')
def list_view(request):
    """Return home page."""
    journals = request.dbsession.query(MyModel).all()
    journals = [journal.to_dict() for journal in journals]
    return {
        "title": "List of my journals:",
        "journal": journals
    }


@view_config(route_name='detail_view', renderer="learning_journal:templates/HB-mockups/detail.jinja2")
def detail_view(request):
    """Return detail view of journal with the input id."""
    journal_id = int(request.matchdict['id'])
    single_journal = request.dbsession.query(MyModel).get(journal_id)
    count = request.dbsession.query(MyModel).count()
    if not (0 < journal_id <= count):
        raise HTTPNotFound
    return {
        'title': 'Single Entry View',
        'Journal': single_journal.to_dict()
    }


@view_config(route_name='update_view', renderer="learning_journal:templates/HB-mockups/edit.jinja2")
def update_view(requset):
    """Return the edit page."""
    return {
        'for_test': 'for_test'
    }


@view_config(route_name='create_view', renderer="learning_journal:templates/HB-mockups/create.jinja2")
def create_view(requset):
    """Return the create page."""
    return {
        'for_test': 'for_test'
    }
