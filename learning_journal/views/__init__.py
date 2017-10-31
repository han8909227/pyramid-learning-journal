from .default import list_view, detail_view, create_view, update_view


def includeme(config):
    """Add view to our config."""
    config.add_view(list_view, route_name='list_view')
    config.add_view(detail_view, route_name='detail_view')
    config.add_view(create_view, route_name='create_view')
    config.add_view(update_view, route_name='update_view')
