
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


from .models import Project
from apps.team.models import Team



@login_required
def projects(request):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
    projects = team.projects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            project = Project.objects.create(team=team, title=title, created_by=request.user)

            messages.info(request, 'The project was added!')
            return redirect('project:projects')
    return render(request, 'project/projects.html', {'team': team, 'projects': projects})