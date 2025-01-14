import re
from itertools import chain
from typing import Union

from django.conf.urls import url
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

from ocfweb.docs.doc import Document
from ocfweb.docs.markdown_based import get_markdown_docs
from ocfweb.docs.views.account_policies import account_policies
from ocfweb.docs.views.buster_upgrade import buster_upgrade
from ocfweb.docs.views.commands import commands
from ocfweb.docs.views.desktop_upgrade import desktop_upgrade
from ocfweb.docs.views.hosting_badges import hosting_badges
from ocfweb.docs.views.index import docs_index
from ocfweb.docs.views.lab import lab
from ocfweb.docs.views.officers import officers
from ocfweb.docs.views.servers import servers
from ocfweb.docs.views.shorturl import shorturl

DOCS = {
    doc.name: doc
    for doc in chain(
        [
            Document(name='/about/officers', title='Officers', render=officers),
            Document(name='/staff/backend/servers', title='Servers', render=servers),
            Document(name='/staff/backend/buster', title='Debian Buster upgrade', render=buster_upgrade),
            Document(name='/staff/backend/nixos', title='NixOS upgrade', render=desktop_upgrade),
            Document(name='/services/account/account-policies', title='Account policies', render=account_policies),
            Document(name='/services/vhost/badges', title='Hosting badges', render=hosting_badges),
            Document(name='/services/lab', title='Computer lab', render=lab),
            Document(name='/services/shell/commands', title='Command reference', render=commands),
            Document(name='/staff/tips/shorturl-tbl', title='ShortURL table', render=shorturl),
        ],
        get_markdown_docs(),
    )
}

REDIRECTS = {
    '/docs/constitution': 'docs/operatingrules/constitution',
    '/docs/bylaws': 'docs/operatingrules/bylaws',
}


def render_doc(request: HttpRequest, doc_name: str) -> HttpResponse:
    """Render a document given a request."""
    doc = DOCS['/' + doc_name]
    if not doc:
        raise Http404()
    return doc.render(doc, request)


def send_redirect(request: HttpRequest, redir_src: str) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
    """Send a redirect to the actual document given the redirecting page."""
    redir_dest = REDIRECTS['/' + redir_src]
    return redirect(reverse('doc', args=(redir_dest,)), permanent=True)


def doc_name(doc_name: str) -> str:
    # we can't actually deal with escaping into a regex, so we just use a whitelist
    assert re.match(r'^/[a-zA-Z0-9\-/]+$', doc_name), 'Bad document name: ' + doc_name
    return doc_name[1:].replace('-', '\\-')


doc_names = '|'.join(map(doc_name, DOCS.keys()))
redir_names = '|'.join(map(doc_name, REDIRECTS.keys()))


urlpatterns = [
    url(r'^$', docs_index, name='docs'),

    # we use a complicated generated regex here so that we have actual
    # validation of URLs (in other words, if you try to make a link to a
    # missing document, it will fail)
    url(fr'^({redir_names})/$', send_redirect),
    url(fr'^({doc_names})/$', render_doc, name='doc'),
]
