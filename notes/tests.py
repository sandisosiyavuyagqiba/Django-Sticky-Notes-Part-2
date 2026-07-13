from django.test import TestCase
from django.urls import reverse

from .models import Author, Note


# Task summary:
# Test that the sticky notes application works as expected.
#
# Pseudocode:
# Create a test author and a test note.
# Check that the note model stores the correct title.
# Check that the note model stores the correct content.
# Check that the note list page opens and displays the note.
# Check that the note detail page opens and displays the note.


class NoteModelTest(TestCase):
    def setUp(self):
        author = Author.objects.create(name="Test Author")
        Note.objects.create(
            title="Test Note",
            content="This is a test note.",
            author=author,
        )

    def test_note_has_title(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, "This is a test note.")


class NoteViewTest(TestCase):
    def setUp(self):
        author = Author.objects.create(name="Test Author")
        Note.objects.create(
            title="Test Note",
            content="This is a test note.",
            author=author,
        )

    def test_note_list_view(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        note = Note.objects.get(id=1)
        response = self.client.get(reverse("note_detail", args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")
