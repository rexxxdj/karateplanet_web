# Generated by Django 3.0.4 on 2020-03-14 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_situation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='situation',
            field=models.FileField(blank=True, null=True, upload_to='uploads/files/', verbose_name='Файл'),
        ),
    ]