from django.db import models


# Task summary:
# Create the database tables for the sticky notes application.
#
# Pseudocode:
# Create an Author model to store the writer's name.
# Create a Note model to store the sticky note details.
# Link each note to an optional author.


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
