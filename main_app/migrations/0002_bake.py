# Generated by Django 2.2 on 2019-06-19 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=200)),
                ('temp', models.CharField(max_length=100)),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Starter')),
            ],
        ),
    ]