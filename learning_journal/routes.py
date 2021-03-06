def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('list_view', '/')
    config.add_route('detail_view', '/journal/{id:\d+}')
    config.add_route('create_view', '/journal/new-entry')
    config.add_route('update_view', '/journal/{id:\d+}/edit-entry')
    config.add_route('delete', '/journal/{id:\d+}/delete')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')





