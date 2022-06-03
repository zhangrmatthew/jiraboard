# Generated by Django 4.0 on 2022-06-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_boards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='boards',
        ),
        migrations.AddField(
            model_name='user',
            name='boards',
            field=models.ManyToManyField(blank=True, related_name='users', to='api.Board'),
        ),
    ]
