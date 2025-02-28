# Generated by Django 3.0.6 on 2020-07-24 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.IntegerField(default=0)),
                ('technical_highlights', models.TextField(default='None')),
                ('acheivements', models.TextField(default='None')),
            ],
        ),
        migrations.CreateModel(
            name='Team_Sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='HAWK/Sponsors')),
                ('name', models.CharField(default='None', max_length=50)),
                ('about_Sponsor_in_short', models.CharField(default='None', max_length=100)),
                ('about_Sponsor', models.TextField(default='None')),
                ('Sponsorship_Package', models.CharField(choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')], default='Gold', max_length=10)),
                ('Link_Website', models.CharField(default='None', max_length=250)),
                ('Link_Instagram', models.CharField(default='None', max_length=250)),
                ('Link_Facebook', models.CharField(default='None', max_length=250)),
                ('Link_Twitter', models.CharField(default='None', max_length=250)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HAWK.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Team_Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(default='None', max_length=20, verbose_name='First Name')),
                ('Middle_Name', models.CharField(default='None', max_length=20, verbose_name='Middle Name')),
                ('last_Name', models.CharField(default='None', max_length=20, verbose_name='Last Name')),
                ('address', models.TextField(default='None', max_length=200, verbose_name='Address')),
                ('image', models.ImageField(default='default.jpg', upload_to='HAWK/TeamMembers')),
                ('Post_In_Team', models.TextField(choices=[('Captain', 'Captain'), ('Captain and Driver', 'Captain and Driver'), ('Vice-Captain', 'Vice-Captain'), ('Vice-Captain and Driver', 'Vice-Captain and Driver'), ('Project Manager', 'Project Manager'), ('Project Manager and Driver', 'Project Manager and Driver'), ('Driver', 'Driver'), ('Codriver', 'Codriver'), ('Tier-1 Member', 'Tier-1 Member'), ('Tier-2 Member', 'Tier-2 Member'), ('None', 'None')], default='None')),
                ('Subsystem', models.TextField(choices=[('Transmission', 'Transmission'), ('Suspension', 'Suspension'), ('Steering', 'Steering'), ('Brakes', 'Brakes'), ('Rollcage', 'Rollcage'), ('Project Management', 'Project Management'), ('None', 'None')], default='None')),
                ('Post_In_Subsystem', models.TextField(choices=[('Head', 'Head'), ('Senior Member', 'Senior Member'), ('Member', 'Member'), ('None', 'None')], default='None')),
                ('PhoneNumber', models.IntegerField(default=0)),
                ('EmailId', models.EmailField(default='none', max_length=254)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HAWK.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='HAWK/images', verbose_name='Image')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HAWK.Team')),
            ],
        ),
    ]
