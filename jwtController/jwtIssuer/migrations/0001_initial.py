# Generated by Django 3.1.7 on 2021-03-17 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reset_code', models.CharField(max_length=500)),
                ('sent_to_email', models.CharField(max_length=500)),
                ('time_sent', models.DateField()),
                ('forUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
