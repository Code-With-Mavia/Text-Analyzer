# views.py - Maawiah
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

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
        # No text entered
        return render(request, 'index.html', {'error': 'Please enter some text to analyze.'})

    analyzed_text = djtext
    purposes = {}

    if removepunc == "on":
        punctuations = '''+!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        analyzed_text = "".join(char for char in analyzed_text if char not in punctuations)
        purposes['removepunc'] = 'Removed Punctuations'

    if fullcaps == "on":
        analyzed_text = analyzed_text.upper()
        purposes['fullcaps'] = 'Changed to Uppercase'

    if newlineremover == "on":
        analyzed_text = analyzed_text.replace('\n', '').replace('\r', '')
        purposes['newlineremover'] = 'Removed New Lines'

    if extraspaceremover == "on":
        analyzed_text = " ".join(analyzed_text.split())
        purposes['extraspaceremover'] = 'Removed Extra Spaces'

    if lowercase == "on":
        analyzed_text = analyzed_text.lower()
        purposes['lowercase'] = 'Changed to Lowercase'

    if charcount == "on":
        char_count = len(analyzed_text)
        purposes['charcount'] = f'Character Count: {char_count}'

    if sentencecount == "on":
        sentence_count = analyzed_text.count('.') + analyzed_text.count('!') + analyzed_text.count('?')
        purposes['sentencecount'] = f'Sentence Count: {sentence_count}'

    if not purposes:
        # No checkbox selected
        return render(request, 'index.html', {'error': 'Please select at least one operation to perform.'})

    params = {
        'purpose': purposes,  # dictionary now
        'analyzed_text': analyzed_text,
    }
    return render(request, 'analyze.html', params)
