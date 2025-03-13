from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Создает группу "Менеджеры" и назначает права'

    def handle(self, *args, **options):
        manager_group, created = Group.objects.get_or_create(name='Менеджеры')

        content_type = ContentType.objects.get_for_model(CustomUser)
        permissions = Permission.objects.filter(content_type=content_type)
        manager_group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS('Группа "Менеджеры" успешно создана и права назначены'))
