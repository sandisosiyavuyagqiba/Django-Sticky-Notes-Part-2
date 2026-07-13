from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


# Task summary:
# Create the page logic for the sticky notes application.
#
# Pseudocode:
# Display all notes.
# Display one selected note.
# Create a new note using a form.
# Update an existing note using the same form.
# Delete a note and return to the list.


def note_list(request):
    notes = Note.objects.all()
    context = {
        "notes": notes,
        "page_title": "List of Notes",
    }
    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
