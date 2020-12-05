

from django.shortcuts import render
from ..models import Show

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Count

from django.db.models import Count


@login_required
#  Will show the show with most notes
def show_most_notes(request):
    # Query count noted and dysplay the three 
    shows = Show.objects.annotate(num_notes=Count('note')).order_by('-num_notes')[:5]
    # Print shows 
    print(shows)
    return render(request, 'lmn/notes/show_most_notes.html', {'shows': shows})

    