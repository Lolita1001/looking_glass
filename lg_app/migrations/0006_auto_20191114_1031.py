# Generated by Django 2.2.6 on 2019-11-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lg_app', '0005_userupload_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preset',
            options={'ordering': ['preset_pack']},
        ),
        migrations.AlterField(
            model_name='userupload',
            name='user_img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images/'),
        ),
    ]