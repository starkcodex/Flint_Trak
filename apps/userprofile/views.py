from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 


@login_required
def myaccount(request):
    teams = request.user.teams.exclude(pk=request.user.userprofile.active_team_id)
    # invitations = Invitation.objects.filter(email=request.user.email, status=Invitation.INVITED)
    # {'teams': teams, 'invitations': invitations}
    return render(request, 'userprofiles/myaccount.html', {'teams': teams})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        messages.info(request, 'the changes was saved')

        return redirect('myaccount')
    return render(request, 'userprofiles/edit_profile.html')



