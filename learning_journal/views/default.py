"""Default."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from ..data import list_journal


@view_config(route_name='list_view', renderer='learning_journal:templates/HB-mockups/index.jinja2')
def list_view(request):
    """."""
    return {
        "title": "List of my journals:",
        "journal": list_journal.Journals
    }


@view_config(route_name='detail_view', renderer="learning_journal:templates/HB-mockups/detail.jinja2")
def detail_view(request):
    """."""
    journal_id = int(request.matchdict['id'])
    if journal_id < 0 or journal_id > len(list_journal.Journals):
        raise HTTPNotFound
    single_journal = list(filter(lambda x: x['id'] == journal_id, list_journal.Journals))[0]
    return {
        'title': 'Single Entry View',
        'Journal': single_journal
    }


@view_config(route_name='update_view', renderer="learning_journal:templates/HB-mockups/edit.jinja2")
def update_view(requset):
    """."""
    return {

    }


@view_config(route_name='create_view', renderer="learning_journal:templates/HB-mockups/create.jinja2")
def create_view(requset):
    """."""
    return {

    }
