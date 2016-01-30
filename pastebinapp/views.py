from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Snippet, SnippetForm
from compile_lang import C_Compiler, CPP_Compiler, CompilerException

import html
import os
import tempfile

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
                   'snip_id': snip_id})

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
    try:
        tempdir = tempfile.mkdtemp()
        comp = get_compiler(snip, tempdir)
        if comp is None:
            raise Http404("No compiler available")
        comp.compile_code()
    except CompilerException as e:
        return render(request, 'pastebinapp/failure.html', {'exception': e})
    finally:
        os.rmdir(tempdir)
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

def get_compiler(snip, tempdir):
    comp = None
    if snip.lang == Snippet.LangType.C:
        comp = C_Compiler(code=snip.text, tempdir=tempdir)
    elif snip.lang == Snippet.LangType.CPP:
        comp = CPP_Compiler(code=snip.text, tempdir=tempdir)
    return comp
