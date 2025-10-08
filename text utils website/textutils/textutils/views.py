# views.py - Maawiah
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

import re

def analyze(request):
    djtext = request.POST.get('text', '')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    charcount = request.POST.get('charcount', 'off')
    sentencecount = request.POST.get('sentencecount', 'off')

    if not djtext.strip():
        return render(request, 'index.html', {'error': 'Please enter some text to analyze.'})

    analyzed_text = djtext
    purposes = {}

    if removepunc == "on":
        # Replace multiple punctuation with single one
        analyzed_text = re.sub(r'([!?.])\1+', r'\1', analyzed_text)
        purposes['removepunc'] = 'Cleaned Excess Punctuations'

    if newlineremover == "on":
        analyzed_text = analyzed_text.replace('\n', ' ').replace('\r', ' ')
        purposes['newlineremover'] = 'Removed New Lines'

    if extraspaceremover == "on":
        analyzed_text = " ".join(analyzed_text.split())
        purposes['extraspaceremover'] = 'Removed Extra Spaces'

    if fullcaps == "on":
        analyzed_text = analyzed_text.upper()
        purposes['fullcaps'] = 'Changed to Uppercase'

    if lowercase == "on":
        analyzed_text = analyzed_text.lower()
        purposes['lowercase'] = 'Changed to Lowercase'

    if charcount == "on":
        purposes['charcount'] = f'Character Count: {len(analyzed_text)}'

    if sentencecount == "on":
        purposes['sentencecount'] = f'Sentence Count: {analyzed_text.count(".") + analyzed_text.count("!") + analyzed_text.count("?")}'

    if not purposes:
        return render(request, 'index.html', {'error': 'Please select at least one operation to perform.'})

    return render(request, 'analyze.html', {'purpose': purposes, 'analyzed_text': analyzed_text})


def features(request):
    return render(request, 'features.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
