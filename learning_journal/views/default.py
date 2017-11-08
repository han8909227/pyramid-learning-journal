"""Default."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from learning_journal.models import MyModel
from datetime import datetime
from pyramid.security import remember, forget, NO_PERMISSION_REQUIRED
from learning_journal.security import is_authenticated


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


@view_config(route_name='create_view',
             renderer="learning_journal:templates/HB-mockups/create.jinja2",
             permission='secret')
def create_view(request):
    """Create a new journal entry, validate it first before putting into db, return home pg."""
    if request.method == 'GET':
        return {}
    if request.method == 'POST':
        if not all(field in request.POST for field in ['title', 'body', 'creation_date']):
            raise HTTPBadRequest
        count = request.dbsession.query(MyModel).count()
        new_journal = MyModel(
            id=count + 1,
            title=request.POST['title'],
            body=request.POST['body'],
            creation_date=request.POST['creation_date']
        )
        request.dbsession.add(new_journal)
        return HTTPFound(request.route_url('list_view'))


@view_config(route_name='update_view',
             renderer="learning_journal:templates/HB-mockups/edit.jinja2",
             permission='secret')
def update_view(request):
    """Update content or title or date of a journal."""
    journal_id = int(request.matchdict['id'])
    journal = request.dbsession.query(MyModel).get(journal_id)
    if not journal:
        raise HTTPNotFound

    if request.method == 'GET':
        return{
            'title': 'Edit Journal',
            'journal': journal.to_dict()
        }
    if request.method == 'POST':
        if request.POST['title'] != '':
            journal.title = request.POST['title']
        if request.POST['body'] != '':
            journal.body = request.POST['body']
        if request.POST['creation_date'] != '':
            journal.creation_date = datetime.strptime(request.POST['creation_date'], '%Y-%m-%d')
        request.dbsession.add(journal)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail_view', id=journal.id))


@view_config(route_name='delete',
             permission='secret')
def delete_expense(request):
    """Delete a journal with given id."""
    journal_id = int(request.matchdict['id'])
    journal = request.dbsession.query(MyModel).get(journal_id)
    if not journal:
        raise HTTPNotFound
    request.dbsession.delete(journal)
    return HTTPFound(request.route_url('list_view'))


@view_config(route_name='login',
             renderer='learning_journal:templates/login.jinja2',
             permission=NO_PERMISSION_REQUIRED)
def login(request):
    """Login route config function."""
    if request.authenticated_userid:
        return HTTPFound(request.route_url('list_view'))

    if request.method == 'GET':
        return {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if is_authenticated(username, password):
            headers = remember(request, username)
            return HTTPFound(request.route_url('list_view'), headers=headers)
        return {
            'error': 'Error: Username/Password does not match!'
        }


@view_config(route_name='logout')
def logout(request):
    """Logout route config function."""
    headers = forget(request)
    return HTTPFound(request.route_url('list_view'), headers=headers)
