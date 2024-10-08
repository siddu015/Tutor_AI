# Generated by Django 5.0.6 on 2024-09-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='content',
            new_name='detail',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='description',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='UserProgress',
        ),
    ]
