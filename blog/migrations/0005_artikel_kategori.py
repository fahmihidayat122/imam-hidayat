# Generated by Django 4.1.4 on 2022-12-14 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='kategori',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.kategori'),
        ),
    ]
