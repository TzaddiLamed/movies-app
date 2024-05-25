from django.shortcuts import render, HttpResponse

context = {
    'movies': ['matrix', 'lego', 'blended']
}

def index(response):
    return render(response, 'movies/index.html', context)

def about(response):
    return render(response, 'movies/about.html', {})
