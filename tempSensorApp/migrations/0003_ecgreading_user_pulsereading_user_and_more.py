from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tempSensorApp', '0002_ecgreading_pulsereading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecgreading',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pulsereading',
            name='user',
        ),
        migrations.RemoveField(
            model_name='temperaturereading',
            name='user',
        ),
        migrations.AddField(
            model_name='ecgreading',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pulsereading',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='temperaturereading',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
