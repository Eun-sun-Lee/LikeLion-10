from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def result(request):
    sentence = str(request.POST.get('sentence')) # sentence textarea 결과값을 str으로 받아옴. -> 안녕 안녕 안녕
    sentence_to_list = sentence.split() # ["안녕","안녕","안녕"]

    dictionary = {}

    for word in sentence_to_list:
        if word in dictionary:
            dictionary[word]+=1
        else:
            dictionary[word]=1
    
    # 사전 형식으로 결과값을 result.html로 넘겨주면 오류 발생 -> list 변환 필요
    word_count = list(dictionary.items()) # [(안녕,3),(은선,1)]
    print(word_count)
    return render(request,"result.html", {'word_count': word_count}) # {result.html 템플릿에서 사용하는 변수 이름 : 위에서 결과값 변수}
