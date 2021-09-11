from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .form import ProjectForm


def hello(request):
    return HttpResponse('Hello World!!')


def projects(request):
    project_details = Project.objects.all()
    context = {'page': 'projects', 'age': 10, 'projects': project_details}
    return render(request, 'projects/projects.html', context=context)


def project(request, pk):
    selected_project = Project.objects.get(id=pk)
    tags = selected_project.tags.all()
    return render(request, 'projects/single-project.html', {'project': selected_project, 'tags': tags})


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def update_project(request, pk):
    project_ = Project.objects.get(id=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project_)
        if form.is_valid():
            form.save()
            return redirect('projects')

    form = ProjectForm(instance=project_)
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def delete_project(request, pk):
    project_ = Project.objects.get(id=pk)

    if request.method == 'POST':
        project_.delete()
        return redirect('projects')

    context = {'project': project_}
    return render(request, 'projects/delete_form.html', context)
