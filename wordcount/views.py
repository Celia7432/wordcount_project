from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import operator


def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddictionary = Counter(wordlist)
    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', \
            {'fulltext':fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})
def about(request):
    return render(request, 'about.html')