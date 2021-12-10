# Generated by Django 3.2.4 on 2021-12-10 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_backend', '0002_auto_20211207_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupConversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('user_admins', models.ManyToManyField(related_name='_messenger_backend_groupconversation_user_admins_+', to='messenger_backend.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('senderId', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('conversation', models.ForeignKey(db_column='conversationId', on_delete=django.db.models.deletion.CASCADE, related_name='messages', related_query_name='message', to='messenger_backend.groupconversation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupConversationThroughModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger_backend.groupconversation')),
                ('last_read_message', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='messenger_backend.groupmessage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger_backend.user')),
            ],
        ),
        migrations.AddField(
            model_name='groupconversation',
            name='users',
            field=models.ManyToManyField(related_name='conversations', through='messenger_backend.GroupConversationThroughModel', to='messenger_backend.User'),
        ),
    ]
