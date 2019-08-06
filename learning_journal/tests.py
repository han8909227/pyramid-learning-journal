"""Testing for pyramid server."""
import pytest
from pyramid import testing
import transaction
from learning_journal.models import (
    MyModel,
    get_tm_session,
)
from learning_journal.models.meta import Base
from datetime import datetime
from faker import Faker
from learning_journal.views.default import list_view, detail_view
from webtest import AppError


@pytest.fixture(scope='session')
def configuration(request):
    """Set up a Configurator instance.

    This Configurator instance sets up a pointer to the location of the
        database.
    It also includes the models from your app's model package.
    Finally it tears everything down, including the in-memory SQLite database.

    This configuration will persist for the entire duration of your PyTest run.
    """
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://postgres:postgres@localhost:5432/testjournals'
    })
    config.include("learning_journal.models")
    config.include("learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a session for interacting with the test database.

    This uses the dbsession_factory on the configurator instance to create a
    new database session. It binds that session to the available engine
    and returns a new session for every call of the dummy_request object.
    """
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Instantiate a fake HTTP Request, complete with a database session.

    This is a function-level fixture, so every new request will have a
    new database session.
    """
    return testing.DummyRequest(dbsession=db_session)


@pytest.fixture
def new_journal():
    """Provide a fixture for one journal."""
    new = MyModel(
        id=1,
        title=u'test journal',
        body=u'test_body',
        creation_date=datetime.now()
    )
    return new


def test_index_returns_list_of_journals_in_dict(dummy_request):
    """Test index return list of journals."""
    response = list_view(dummy_request)
    assert 'journal' in response
    assert isinstance(response['journal'], list)


def test_journal_exists_and_is_in_list(dummy_request, new_journal):
    """Test journal exists in the list."""
    dummy_request.dbsession.add(new_journal)
    # dummy_request.dbsession.flush()
    # journal = new_journal()
    response = list_view(dummy_request)
    assert new_journal.to_dict() in response['journal']


def test_detail_view_shows_journal_detail(dummy_request, new_journal):
    """Test detail view show journal details."""
    dummy_request.dbsession.add(new_journal)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 1
    response = detail_view(dummy_request)
    assert response['Journal'] == new_journal.to_dict()


@pytest.fixture(scope="session")
def testapp(request):
    """Initialte teh test app."""
    from webtest import TestApp
    from pyramid.config import Configurator

    def main():
        settings = {
            'sqlalchemy.url': 'postgres://postgres:postgres@localhost:5432/testjournals'
        }  # points to a database
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('learning_journal.routes')
        config.include('learning_journal.models')
        config.include('learning_journal.security')
        config.scan()
        return config.make_wsgi_app()

    app = main()

    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)  # builds the tables

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)
    return TestApp(app)


FAKE = Faker()
JOURNALS = []
for i in range(10):
    journals = MyModel(
        id=i,
        title=FAKE.file_name(),
        body=FAKE.paragraph(),
        creation_date=FAKE.date_time()
    )
    JOURNALS.append(journals)


@pytest.fixture(scope="session")
def fill_the_db(testapp):
    """Fill the db with fake journal entries."""
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(JOURNALS)


def test_home_route_has_table(testapp):
    """Test route has table."""
    response = testapp.get("/")
    assert len(response.html.find_all('body')) == 1
    assert len(response.html.find_all('p')) == 0


def test_home_route_with_journals_has_rows(testapp, fill_the_db):
    """Test home route has rows."""
    response = testapp.get("/")
    assert len(response.html.find_all('p')) == 10


def test_detail_route_with_journal_detail(testapp, fill_the_db):
    """Test if detail papge has proper response.."""
    response = testapp.get("/journal/1")
    assert 'ID: 1' in response.ubody


@pytest.fixture
def journal_info():
    """Create a info dictionary for edit or create later."""
    info = {
        'title': 'testing',
        'body': 'testing_body',
        'creation_date': '2017-11-02'
    }
    return info


@pytest.fixture
def edit_info():
    """Create a dict for editing purpose."""
    info = {
        'title': 'edited journal',
        'body': 'I just changed the journal created in above test',
        'creation_date': ''
    }
    return info


@pytest.fixture
def login(testapp):
    """I will log you in, please don't hack me."""
    secret = {
        'username': 'hbao',
        'password': 'secret'
    }
    testapp.post('/login', secret)


@pytest.fixture
def logout(testapp):
    """I will log you out from the session."""
    testapp.get('/logout')


@pytest.fixture
def csrf_token(testapp):
    """Will get the csrf token."""
    get_tk = testapp.get('/journal/new-entry')
    token = get_tk.html.find('input', {'name': 'csrf_token'})['value']
    return token


def test_create_view_successful_post_redirects_home(testapp, journal_info, login, csrf_token):
    """Test create view directs to same loc."""
    journal_info['csrf_token'] = csrf_token
    response = testapp.post("/journal/new-entry", journal_info)
    assert response.location == 'http://localhost/'


def test_create_view_successful_post_actually_shows_home_page(testapp, journal_info, csrf_token):
    """Test create view folow up with detail page."""
    journal_info['csrf_token'] = csrf_token
    response = testapp.post("/journal/new-entry", journal_info)
    next_page = response.follow()
    assert "testing" in next_page.ubody


def test_edit_method_successful_updates(testapp, edit_info, csrf_token):
    """Test if content is updated successfully."""
    edit_info['csrf_token'] = csrf_token
    response = testapp.post('/journal/1/edit-entry', edit_info)
    next_page = response.follow()
    assert 'edited journal' in next_page.ubody


def test_edit_method_successful_updates_and_directs_detail_view(testapp, edit_info, csrf_token):
    """Test after updating we get re-directed to detail view."""
    edit_info['csrf_token'] = csrf_token
    response = testapp.post('/journal/1/edit-entry', edit_info)
    assert response.location == 'http://localhost/journal/1'


def test_edit_method_return_httpnotfound(testapp, edit_info, csrf_token):
    """Assert if a http not found error(raised by apperror) is popped from invalid post req (mt)."""
    try:
        testapp.post('/journal/200/edit-entry', {'csrf_token': csrf_token})
    except AppError as err:
        assert '404 Not Found' in err.args[0]


def test_create_method_return_httpnotfound_with_no_var(testapp, csrf_token):
    """Assert if a http not found error(raised by apperror) is popped from invalid post req (mt)."""
    try:
        testapp.post('/journal/new-entry', {'csrf_token': csrf_token})
    except AppError as err:
        assert '400 Bad Request' in err.args[0]


def test_no_create_journal_nav_tab_before_login(testapp, logout):
    """Before login you won't see the new post tab."""
    response = testapp.get('/')
    assert 'New Post' not in response.ubody and 'Login' in response.ubody


def test_create_journal_nav_tab_after_login(testapp, login):
    """Test login in tab appears after you logged in."""
    response = testapp.get('/')
    assert 'New Post' in response.ubody and 'Logout' in response.ubody


def test_both_auth_and_unauth_user_can_access_home_pg(testapp, logout):
    """Test whether an authorized and an unauthorized user can access home route."""
    response = testapp.get('/')
    logout
    response_1 = testapp.get('/')
    assert 'Han\'s Blog' in response.ubody and response_1.ubody


def test_both_auth_and_unauth_user_can_access_detail_pg(testapp, login, logout):
    """Test whether both authorized and unauthroized user can access a detail route."""
    response = testapp.get('/journal/5')
    logout
    response_1 = testapp.get('/journal/5')
    assert 'ID: 5' in response.ubody and response_1.ubody


def test_wrong_password_wont_login(testapp):
    """Test if we can login with a wrong password."""
    response = testapp.post('/login', {'username': 'hbao', 'password': 'notmypassword'})
    assert 'Error: Username/Password does not match!' in response


def test_wrong_username_wont_login(testapp):
    """Test if we can login with a wrong username."""
    response = testapp.post('/login', {'username': 'notmyusername', 'password': 'secret'})
    assert 'Error: Username/Password does not match!' in response

