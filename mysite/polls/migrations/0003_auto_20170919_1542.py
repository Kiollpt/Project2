# Generated by Django 2.0.dev20170906232138 on 2017-09-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('text', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(verbose_name='posted')),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]