from pyramid.response import Response


def list_view(request):
    """View of the indexes."""
    with open('learning_journal/templates/HB-mockups/index.html', 'r') as fn:
        return Response(fn.read())


def update_view(request):
    """View of single entry."""
    with open('learning_journal/templates/HB-mockups/edit.html', 'r') as fn:
        return Response(fn.read())


def create_view(request):
    """Create a new entry."""
    with open('learning_journal/templates/HB-mockups/create.html', 'r') as fn:
        return Response(fn.read())


def detail_view(request):
    """."""
    with open('learning_journal/data/entry.html', 'r') as fn:
        return Response(fn.read())

