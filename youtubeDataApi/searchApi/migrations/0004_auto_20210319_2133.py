from django.db import migrations
from django.conf import settings

#Data Migration to insert API keys
class Migration(migrations.Migration):

    dependencies = [
        ('searchApi', '0002_apikeys'),
    ]

    def insertData(apps, schema_editor):
        ApiKeys = apps.get_model('searchApi', 'ApiKeys')
        for key in settings.YOUTUBE_SEARCH_API_KEYS:
            if key == settings.YOUTUBE_SEARCH_CURRENT_API_KEY:
                api_key = ApiKeys(api_key=key, is_active=True)
                api_key.save()
            else:
                api_key = ApiKeys(api_key=key)
                api_key.save()

    operations = [
        migrations.RunPython(insertData),
    ]
