from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def projects(request):
    # return HttpResponse("list of projects")
    return render(request, "projects/projects.html")

def singleProject(request, pk):
    # return HttpResponse(f"Project number {str(pk)}")
    return render(request, "projects/singleProject.html")