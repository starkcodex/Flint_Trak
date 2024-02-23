from django.urls import path
from .views import add_team, team, edit, activate_team


app_name = 'team'

urlpatterns = [
    path('', add_team, name='add_team'),
    path('edit', edit, name='edit'),    
    path('activate_team/<int:team_id>', activate_team, name='activate_team'),  
    path('<int:team_id>/', team, name='team'),
]