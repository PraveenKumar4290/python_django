# Generated by Django 4.2.16 on 2024-11-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]