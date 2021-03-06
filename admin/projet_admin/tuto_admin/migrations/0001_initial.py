# Generated by Django 2.2.7 on 2019-11-08 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='', verbose_name='images')),
                ('statut', models.BooleanField(default=False)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_up', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('statut', models.BooleanField(default=False)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_up', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sous_categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='', verbose_name='images')),
                ('statut', models.BooleanField(default=False)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_up', models.DateTimeField(auto_now=True)),
                ('categore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='tuto_admin.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to='', verbose_name='images')),
                ('statut', models.BooleanField(default=False)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_up', models.DateTimeField(auto_now=True)),
                ('sous_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sous_cat', to='tuto_admin.Sous_categorie')),
                ('tag', models.ManyToManyField(to='tuto_admin.Tag')),
            ],
        ),
    ]
