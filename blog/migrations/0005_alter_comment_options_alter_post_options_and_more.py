# Generated by Django 4.2.15 on 2024-08-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='post',
            name='feild_1',
            field=models.CharField(default='test'),
            preserve_default=False,
        ),
    ]
