import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "ordering": ["id"],
                "permissions": [("can_cancel_mailing", "Can cancel mailing")],
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.AlterField(
            model_name="mailing",
            name="finish_send_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 12, 11, 19, 4, 14, 513083),
                verbose_name="Дата и время окончания отправки",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="first_send_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 12, 10, 19, 4, 14, 513083),
                verbose_name="Дата и время первой отправки",
            ),
        ),
    ]
