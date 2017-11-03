"""Default."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from learning_journal.models import MyModel
from datetime import datetime


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


@view_config(route_name='create_view', renderer="learning_journal:templates/HB-mockups/create.jinja2")
def create_view(requset):
    """Create a new journal entry, validate it first before putting into db, return home pg."""
    if requset.method == 'GET':
        return {}
    if requset.method == 'POST':
        if not all([field in requset.POST for field in ['id', 'title', 'body', 'creation_date']]):
            raise HTTPBadRequest
        new_journal = MyModel(
            id=requset.POST['id'],
            title=requset.POST['title'],
            body=requset.POST['body'],
            creation_date=requset.POST['creation_date']
        )
        requset.dbsession.add(new_journal)
        return HTTPFound(requset.route_url('list_view'))


@view_config(route_name='update_view', renderer="learning_journal:templates/HB-mockups/edit.jinja2")
def update_view(request):
    """Return the edit page."""
    journal_id = int(request.matchdict['id'])
    journal = request.dbsession.query(MyModel).get(journal_id)
    if not journal:
        raise HTTPFound

    if request.method == 'GET':
        return{
            'title': 'Edit Journal',
            'journal': journal.to_dict()
        }

    if request.method == 'POST':
        journal.title = request.POST['title']
        journal.body = request.POST['body']
        journal.creation_date = datetime.strptime(request.POST['creation_date'], '%Y-%m-%d')
        request.dbsession.add(journal)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail_view', id=journal_id))
