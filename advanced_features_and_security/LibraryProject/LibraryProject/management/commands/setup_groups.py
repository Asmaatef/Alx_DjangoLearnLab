from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book  

class Command(BaseCommand):
    help = 'Set up initial groups and permissions'

    def handle(self, *args, **kwargs):
        groups = {
            "Editors": ["can_create", "can_edit"],
            "Viewers": ["can_view"],
            "Admins": ["can_create", "can_edit", "can_delete", "can_view"],
        }

        content_type = ContentType.objects.get_for_model(Book)
        for group_name, perms in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in perms:
                permission, _ = Permission.objects.get_or_create(
                    codename=perm,
                    content_type=content_type,
                )
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Groups and permissions successfully set up!'))
