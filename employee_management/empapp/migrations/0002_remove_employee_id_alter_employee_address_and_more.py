# Generated by Django 5.0.6 on 2024-06-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='empid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lname',
            field=models.CharField(max_length=100),
        ),
    ]
