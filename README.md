# Youtube-Data-API-Integration

### Description
```
A cron job runs (every minute) in background which fetches data from youtube and saves it in database.It creates cron_job.log (log file is created on Desktop).
Also exposed two GET {/search and /videos-details} endpoints.
```

## Instructions

#### Imp - Add keys in youtubeDataApi/settings.py (YOUTUBE_SEARCH_API_KEYS) before starting project.

### Install Dependencies
```bash
--- pip install -r requirements.txt 
```

### Create and Apply Migrations
```bash
--- python manage.py makemigrations
--- python manage.py migrate
```

### Add Cron Job
```bash
--- python manage.py crontab add
--- python manage.py crontab show (check if added)
```

### Remove Cron Job
```bash
--- python manage.py crontab remove
```

### Run Server
```bash
--- python manage.py runserver
```

### Docker
```bash
--- docker-compose build
--- docker-compose up
```

### API Endpoints
```bash
--- /videos-details -> page_number (optional).Returns 1st page by default.
--- /search  -> search_keyword (mandatory).Returns details of videos where keyword is found in title or description.
```