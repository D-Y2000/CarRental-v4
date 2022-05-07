# Generated by Django 4.0.3 on 2022-05-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_rename_make_model_make_id_rename_model_model_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='vehicle',
            name='options',
            field=models.ManyToManyField(blank=True, null=True, related_name='vehicle', to='vehicle.option'),
        ),
    ]