# Generated by Django 4.1.2 on 2022-10-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"ordering": ["last_name", "first_name"]},
        ),
        migrations.AlterModelOptions(
            name="bookinstance",
            options={"ordering": ["due_back"]},
        ),
        migrations.RemoveField(
            model_name="bookinstance",
            name="date_of_birth",
        ),
        migrations.RemoveField(
            model_name="bookinstance",
            name="date_of_death",
        ),
        migrations.RemoveField(
            model_name="bookinstance",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="bookinstance",
            name="last_name",
        ),
        migrations.AddField(
            model_name="author",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="author",
            name="date_of_death",
            field=models.DateField(blank=True, null=True, verbose_name="Died"),
        ),
        migrations.AddField(
            model_name="author",
            name="first_name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="author",
            name="last_name",
            field=models.CharField(default="", max_length=100),
        ),
    ]
