# Generated by Django 2.2.13 on 2021-01-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0011_subject_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='batches',
            field=models.ManyToManyField(related_name='department_batches', to='academics.Batch'),
        ),
    ]
