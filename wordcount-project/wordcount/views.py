from django.http import HttpResponse
#this enables templating
from django.shortcuts import render
import operator 

#using templates from templates folder
def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in ('--', '??'):
            cpt = 0;
        else:
            if word in worddictionary:
            #increase cpt 
                 worddictionary[word] += 1
            else:
            #add to the dictionary
                 worddictionary[word] = 1

        
    #Sorting list 
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)


    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})