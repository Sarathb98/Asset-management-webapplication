# Generated by Django 3.1.6 on 2021-09-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ide', models.CharField(max_length=20)),
                ('dev', models.CharField(max_length=20)),
                ('dep', models.CharField(max_length=20)),
                ('own', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=20)),
                ('sts', models.CharField(max_length=20)),
            ],
        ),
    ]