The Ways of the World
=====================

## Deployment ##
Our site is deployed on a Linode server and runs behind nginx using fastcgi.
Everything is located in `/django/bases/`.
[This] guide was useful in deploying the site.
Fastcgi spawns a number of processes so to keep track of which ones it spawns,
start it with `./manage.py runfcgi host=127.0.0.1 port=8080 pidfile=django.pid`. The pidfile is to keep track of the process ids spawned by fastcgi. Check out the django [docs] to learn about serving static files.
Restart nginx with `/etc/init.d/nginx restart` and restart django with `/etc/init.d/django restart`. Restarting django reloads all django/FastCGI projects at once.

[This]: https://code.djangoproject.com/wiki/DjangoAndNginx
[docs]: https://docs.djangoproject.com/en/dev/howto/static-files/

## When Things Go Wrong ##
Check out [this] if you're having trouble with the path info env variable.

[this]: http://neithere.net/dev/notes/nginx-fcgi-django/
