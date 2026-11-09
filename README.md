# Bootstrap Django — Class Project

A simple multi-page website built with **Django 6.1** and **Bootstrap**, as part of our Django class.
It demonstrates the core Django concepts we covered: projects, apps, URLs, views, templates, and static files — plus deployment to Render.

## Pages

| URL | View | Template |
|-----|------|----------|
| `/` | `index` | `index.html` |
| `/service/` | `service` | `service.html` |
| `/fruit/` | `fruit` | `fruit.html` |
| `/contact/` | `contact` | `contact.html` |
| `/admin/` | Django admin | — |

## What this project teaches (class concepts)

### 1. Project vs. App
- **Project** = `bootstrapdjango` — the overall site (settings, root URL config, WSGI entry point).
- **App** = `myapp` — a self-contained module with its own views, urls, templates, static files, and (future) models.

### 2. The URL → View → Template flow
1. A request hits `bootstrapdjango/urls.py`, which forwards app URLs with `include('myapp.urls')`.
2. `myapp/urls.py` maps each path to a view function, e.g. `path('fruit/', views.fruit)`.
3. Each view in `myapp/views.py` returns `render(request, 'fruit.html')`.
4. Django finds the template in `myapp/templates/` and returns the HTML.

### 3. Template inheritance
`templates/base.html` holds the shared layout (navbar, footer, script includes).
The page templates (`index.html`, `fruit.html`, …) extend it and only fill in the unique content.

### 4. Static files
CSS, JavaScript, and images live in `myapp/static/` (Bootstrap, jQuery, custom styles, images).
Referenced with the `{% static %}` template tag. In production they are collected into
`STATIC_ROOT` (`bootstrapdjango/staticfiles/`) by `collectstatic` and served by **WhiteNoise**.

### 5. Settings that matter (`bootstrapdjango/settings.py`)
- `INSTALLED_APPS` — which apps are active (`myapp` was added here).
- `MIDDLEWARE` — request/response pipeline; WhiteNoise sits right after `SecurityMiddleware`.
- `DEBUG` — reads from the environment: `True` in development, `False` in production.
- `STATIC_URL` / `STATIC_ROOT` — where static files are addressed from and collected to.

### 6. Models & Admin (next steps)
`myapp/models.py` is ready for our first model — once we add one and run
`makemigrations` / `migrate`, it will automatically appear in the `/admin/` site.

## Running locally

```bash
# activate the existing virtual environment (from the project root)
. bin/activate

cd bootstrapdjango

# with debug on (Django serves static files itself in dev)
DEBUG=True python3 manage.py runserver
```

Then visit http://127.0.0.1:8000/

Commands this project uses:

```bash
python3 manage.py migrate           # apply migrations to the database
python3 manage.py createsuperuser   # create an admin login
python3 manage.py collectstatic     # gather static files into STATIC_ROOT
```

## Deployment (Render)

- **Build command:**
  `pip install -r requirements.txt && cd bootstrapdjango && python manage.py collectstatic --noinput`
- **Start command:**
  `cd bootstrapdjango && gunicorn bootstrapdjango.wsgi`

Key production settings:

- `DEBUG=False` (default when the env var isn't set)
- Static files are served by WhiteNoise from `STATIC_ROOT`
- Gunicorn serves the app instead of the development server

> **Note:** the site uses SQLite (`db.sqlite3`), and Render's filesystem is ephemeral —
> database data is wiped on every redeploy. Fine for a demo; use a managed database for real data.

## Tech stack

- Python 3.14 / Django 6.1
- Bootstrap + jQuery (static assets)
- WhiteNoise (static file serving)
- Gunicorn (production server)
- Render (hosting)
