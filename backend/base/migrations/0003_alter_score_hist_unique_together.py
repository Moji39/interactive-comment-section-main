# Generated by Django 4.0.6 on 2022-07-13 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_score_hist_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='score_hist',
            unique_together={('user', 'comment')},
        ),
    ]
