from django.shortcuts import get_object_or_404, render
from django.db.utils import ProgrammingError

from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Snippet, SnippetForm
from compile_lang import C_Compiler, CPP_Compiler, CompilerException, Rust_Compiler
from .tasks import test, fwd_req

import html
import os
import tempfile
import time

def index(request): 
    latest = Snippet.objects.order_by('pk').reverse()[0:5]
    context = {
      'latest_snips': latest
    }
    return render(request, 'pastebinapp/index.html', context)

def code(request, snip_id):
    try:
        snip = Snippet.objects.get(pk=snip_id)
    except Snippet.DoesNotExist:
        raise Http404("Snippet does not exist")
    return render(request, 'pastebinapp/code.html', 
                  {'code': snip.text, 'title': snip.title,
                   'snip_id': snip_id, 'lang': snip.lang})

def enter_snip(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pastebinapp/')
    else:
        form = SnippetForm()

    return render(request, 'pastebinapp/enter_snip.html', {'form': form})

def compile_snip(request, snip_id):
    try:
        snip = Snippet.objects.get(pk=snip_id)
    except Snippet.DoesNotExist:
        raise Http404("Snippet does not exist")
    print('forwarding')
    result = fwd_req(Snippet.app_to_pb_comp_lang_map[snip.lang],
                     snip.text)
    if result is None:
      print('compiler unavailable')
      return render(request, 'pastebinapp/failure.html')
    print(result)
    return render(request, 'pastebinapp/success.html')

def edit_snip(request, snip_id):
    snip = get_object_or_404(Snippet, pk=snip_id)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snip)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pastebinapp/')
    else:
        form = SnippetForm(instance=snip)

    return render(request, 'pastebinapp/enter_snip.html', {'form': form})
