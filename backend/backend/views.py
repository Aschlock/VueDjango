from django.http import HttpResponse

def view(request):
    return HttpResponse("Here's the text of the Web page.")
