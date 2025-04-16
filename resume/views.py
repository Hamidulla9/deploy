from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'base.html', context)


def about(request):
    context = {}
    return render(request, 'resume/about.html', context)


def contact(request):
    context = {}
    return render(request, 'resume/contact.html', context)


def works(request):
    context = {}
    return render(request, 'resume/works.html', context)


def resume(request):
    context = {}
    return render(request, 'resume/resume.html', context)


