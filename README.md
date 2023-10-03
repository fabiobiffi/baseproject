# Base Project

# Preliminary information
write here

# Development
## Git hooks
Open with a terminal and execute

```bash
git config core.hooksPath git-hooks
```

## Run Base Project

### if you are on linux
Ensure that all directories such `static` or `uploaded` have right permissions
(no root owner).

### Simil prod environment
If you want to run BaseProject in a "simil-prod" environment

```bash
docker compose up
```
after that you can visit http://localhost/

### Developing environment
if you want to work and debug on BaseProject

```bash
docker compose up
```

after that open a new terminal and

```bash
docker exec -it application bash
```

```bash
cd src/
python manage.py runserver 0.0.0.0:8001 --insecure
```
NB: `--insecure` is mandatory if you want see static files with `DEBUG=False`

Now you can visit http://localhost:8001
