# Sticky Notes Django Application Part 2

Sticky Notes is a simple Django web application that allows users to manage
short notes through a browser. The application demonstrates the basic Django
workflow of using models, views, URLs, templates, forms, static files, a
SQLite database, and unit tests.

## About The App

The app allows a user to:

- view all sticky notes
- open a single sticky note
- create a new sticky note
- update an existing sticky note
- delete a sticky note

Each note is saved in the database and displayed through Django templates.
The pages are styled with a CSS file so that the notes are easier to read and
use.

## Main Features

- A home page that displays all saved notes.
- A detail page for viewing one note.
- A form page for creating and editing notes.
- Delete functionality for removing notes.
- Django admin support for managing note records.
- SQLite database storage.
- Unit tests for the note model and note views.

## How It Works

The application uses Django models to describe the note data that must be
stored. Django forms are used to collect information from the user when a note
is created or edited. The views control what happens when a user visits a page,
and the URL files connect each page address to the correct view.

Templates are used to display the pages in the browser. Static CSS is used to
style the application and make the notes look neat and readable.

The tests check that the note model stores the correct information and that
the list and detail pages load successfully.

## Running The App

Open the project folder in VS Code or a terminal. Make sure the terminal is in
the same folder as `manage.py`, then run:

```bash
python manage.py migrate
python manage.py runserver
```

Open the app in your browser:

```text
http://127.0.0.1:8000/
```

## Running The Tests

To run the unit tests, use:

```bash
python manage.py test
```

The tests check the note title, note content, note list page, and note detail
page.

## Admin Access

To use the Django admin area, create a superuser:

```bash
python manage.py createsuperuser
```

Then start the server and open:

```text
http://127.0.0.1:8000/admin/
```

## What I Learned

This project helped me understand how the main parts of a Django application
work together. I learned how models store data, how views control page logic,
how URLs connect pages to views, how templates display information, how forms
allow users to add or update data, and how unit tests check that the
application works correctly.
