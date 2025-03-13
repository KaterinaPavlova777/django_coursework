import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "mailing",
            "0003_rename_mailing_response_mailingattempt_mail_server_response_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="finish_send_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 12, 15, 13, 49, 54, 607878),
                verbose_name="Дата и время окончания отправки",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="first_send_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 12, 14, 13, 49, 54, 607878),
                verbose_name="Дата и время первой отправки",
            ),
        ),
    ]
