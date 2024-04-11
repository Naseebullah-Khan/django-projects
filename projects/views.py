from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
def projects(request):
    return HttpResponse("list of projects")

def singleProject(request, pk):
    return HttpResponse(f"Project number {pk}")