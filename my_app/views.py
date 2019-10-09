from django.shortcuts import render
from my_app.models import Cronjob


def index(request):
    if request.method == "POST":
        title = request.POST.get('Titel')
        url = request.POST.get('Url')
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        tablefill = Cronjob()

        tablefill.title = title
        tablefill.url = url
        tablefill.username = username
        tablefill.password = password
        tablefill.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')



