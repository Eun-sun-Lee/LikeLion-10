from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def result(request):
    sentence=str(request.POST.get('sentence'))
    sentence_to_list=sentence.split()

    dictionary={}
    for word in sentence_to_list:
        if word in dictionary:
            dictionary[word]+=1
        else: dictionary[word]=1
        
    
    word_count=list(dictionary.items())
    print(word_count)
    return render(request,"result.html",{'word_count': word_count})

# Create your views here.
