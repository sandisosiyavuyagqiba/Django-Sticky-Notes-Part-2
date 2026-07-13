from django import forms

from .models import Note


# Task summary:
# Create a form for adding and editing sticky notes.
#
# Pseudocode:
# Use Django's ModelForm.
# Connect the form to the Note model.
# Display title, content, and author fields.


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "author"]
