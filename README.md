The Ways of the World
=====================

## Deployment ##
Our site is deployed on a Linode server and runs behind nginx using fastcgi.
[This] guide was useful in deploying the site.
Fastcgi spawns a number of processes so to keep track of which ones it spawns,
start it with `./manage.py runfcgi host=127.0.0.1 port=8080 pidfile=django.pid`. The pidfile is to keep track of the process ids spawned by fastcgi.

[This]: https://code.djangoproject.com/wiki/DjangoAndNginx
