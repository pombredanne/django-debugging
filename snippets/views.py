from django.http import HttpResponse

from snippets.models import Snippet

def snippet_show(request, id):
    snip = Snippet.objects.get(id=id)
    return HttpResponse("Snippet: %s, Title: %s" % (id, snip.title), content_type="text/plain")


def snippet_all(request):
    """
    http://localhost:8123/snippet/all
    """
    snip_all = Snippet.objects.all()[:10]

    response = ""
    for snip in snip_all:
        response = "%s\n Snippet: %s, Title: %s, User: %s" % (response, snip.id, snip.title, snip.user.username)

    return HttpResponse(response, content_type="text/plain")


def snippet_update(request, id):
    """
    http://localhost:8123/snippet/update/1?title=haha2
    """
    snip = Snippet.objects.get(id=id)
    title = request.GET.get('title', None)
    if title:
        snip.title = title
        snip.save()
        response = "%s updated" % id
    else:
        response = "nothing changed"

    return HttpResponse(response, content_type="text/plain")