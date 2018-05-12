from django.shortcuts import render


def word_list(request):
    return render(request,'dostdict/word_list.html')
# Create your views here.
