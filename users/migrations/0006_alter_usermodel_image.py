# Generated by Django 4.2.2 on 2023-06-11 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_usermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_photos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'heif', 'jpeg', 'heic'])]),
        ),
    ]
