# Design Diagram

## App Structure
```mermaid
flowchart TD
    User[User] --> Browser[Browser]
    Browser --> URLs[Django URLs]
    URLs --> Views[Views]
    Views --> Templates[Templates]
    Views --> Forms[Forms]
    Views --> Models[Models: Post / Author]
    Models --> Database[(Database)]
    Forms --> Models
    Templates --> User
```

## Main Components
- URLs: route requests to the correct view
- Views: handle listing, detail, create, update, and delete actions
- Forms: collect and validate user input
- Models: store posts and authors
- Templates: display the user interface
- Tests: validate list, detail, create, update, and delete behaviour
