import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mailing", "0002_alter_mailing_options_alter_mailing_finish_send_at_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mailingattempt",
            old_name="mailing_response",
            new_name="mail_server_response",
        ),
        migrations.AlterField(
            model_name="mailing",
            name="finish_send_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 12, 14, 23, 2, 49, 722022),
                verbose_name="Дата и время окончания отправки",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="first_send_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 12, 13, 23, 2, 49, 722022),
                verbose_name="Дата и время первой отправки",
            ),
        ),
    ]
