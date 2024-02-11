# Generated by Django 5.0.2 on 2024-02-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('Marketing', 'Marketing'), ('Admin', 'Admin'), ('None', 'None'), ('IT', 'IT'), ('Sales', 'Sales')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('IT Assistant', 'IT Assistant'), ('Marketing Executive', 'Marketing Executive'), ('Sales Executive', 'Sales Executive'), ('IT Manager', 'IT Manager'), ('Marketing Manager', 'Marketing Manager')], default='None', max_length=100),
        ),
    ]