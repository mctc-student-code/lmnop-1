from django.shortcuts import render, redirect, get_object_or_404
from ..models import Venue, Artist, Note, Show
from ..forms import VenueSearchForm, NewNoteForm, ArtistSearchForm, UserRegistrationForm

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from lmnop_project import helpers


@login_required
def new_note(request, show_pk):

    show = get_object_or_404(Show, pk=show_pk)

    if request.method == 'POST':
        form = NewNoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.show = show
            note.photo = request.photo
            note.save()

<<<<<<< HEAD
            return redirect('note_detail', note_pk=note.pk)
=======
            return redirect('my_user_profile')
>>>>>>> 77d5337f4edb4279c64a387de8bc01b0dc0e9af1

    else :
        form = NewNoteForm()

    return render(request, 'lmn/notes/new_note.html' , { 'form': form , 'show': show })


def latest_notes(request):
    notes = Note.objects.all().order_by('-posted_date')

    # get page number to be supplied to pagination for page number display
    page = request.GET.get('page')
    # Calls helper function to paginate records. (request, list of objects, how many entries per page)
    #TODO change number of objects supplied to 20 before deployment
    notes = helpers.pg_records(page, notes, 5)

    return render(request, 'lmn/notes/note_list.html', { 'notes': notes })


def notes_for_show(request, show_pk):
    # Notes for show, most recent first
    notes = Note.objects.filter(show=show_pk).order_by('-posted_date')
<<<<<<< HEAD
    show = Show.objects.get(pk=show_pk)
    return render(request, 'lmn/notes/note_list.html', { 'show': show, 'notes': notes })
=======

    show = Show.objects.get(pk=show_pk)  
    return render(request, 'lmn/notes/notes_for_show.html', { 'show': show, 'notes': notes })
>>>>>>> 77d5337f4edb4279c64a387de8bc01b0dc0e9af1


def note_detail(request, note_pk):
    #only show user's notes if logged in
    note = get_object_or_404(Note, pk=note_pk)
    if request.user == note.user:
        form = NewNoteForm(instance=note)  # Pre-populate with data from this NOte instance
        return render(request, 'lmn/notes/note_detail.html', {'note': note, 'form': form} )
    
    return render(request, 'lmn/notes/note_detail.html', {'note': note} )
  
    
@login_required
def edit_note(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk)
    #need to get the show Id as saving the note requires that
    show = get_object_or_404(Show, pk= note.show_id)
    if note.user != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST' :
        form = NewNoteForm(request.POST, request.FILES, instance=note)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.show = show
            note.save()
<<<<<<< HEAD

            return redirect('note_detail', note_pk=note.pk)


=======
           
            return redirect('my_user_profile')

          
>>>>>>> 77d5337f4edb4279c64a387de8bc01b0dc0e9af1
@login_required #can only delete own notes
def delete_note(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk)
    if note.user == request.user:
        note.delete()
        #show latest notes after deleting the note
        notes = Note.objects.all().order_by('-posted_date')
        return redirect('my_user_profile')
    else:
        return HttpResponseForbidden()
