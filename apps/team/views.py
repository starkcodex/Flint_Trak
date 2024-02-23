from django.shortcuts import get_object_or_404, render, redirect
from .models import Team
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id, status= Team.ACTIVE, members__in=[request.user])

    return render(request, 'team/team.html', {'team': team})

@login_required
def activate_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id, status=Team.ACTIVE, members__in=[request.user])
    userprofile = request.user.userprofile
    userprofile.active_team_id = team.id
    userprofile.save()

    messages.info(request, 'The team was activated')

    return redirect('team:team', team_id=team.id)



@login_required
def add_team(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            team = Team.objects.create(title=title, created_by=request.user)
            team.members.add(request.user)
            team.save()

            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id
            userprofile.save()
            return redirect('myaccount')
        
    return render(request, 'team/add_team.html')



@login_required
def edit(request):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE, members__in=[request.user])

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            team.title = title
            team.save()

            messages.info(request, 'The changes was saved')
            return redirect('team:team', team_id=team.id)
    return render(request, 'team/edit.html', {'team': team})