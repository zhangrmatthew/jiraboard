# Generated by Django 4.0 on 2022-06-03 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_user_boards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='boards',
            field=models.ManyToManyField(blank=True, related_name='users', to='api.Board'),
        ),
    ]