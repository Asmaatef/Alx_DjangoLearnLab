# Permissions and Groups Setup

## Groups and Permissions
- **Viewers**: Can view books.
- **Editors**: Can create and edit books.
- **Admins**: Full access (view, create, edit, delete).

## Adding New Permissions
To add new permissions:
1. Update the `Meta` class in the model.
2. Run `python manage.py makemigrations` and `python manage.py migrate`.
3. Assign permissions to groups via the admin panel or the `setup_groups.py` command.

## Protecting View
Use `@permission_required` decorator to enforce permissions on views. Example:
```python
@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    
