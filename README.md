# pinkhatbeard.com
Homelessgaffer is dead; long live pinkhatbeard.

## Colophon
- Server side: Python, Flask
- DB: SQL, SQLite, SQL-Alchemy
- Client Side: Bootstrap

## Use
On OS X or Linux (Windows, you're on your own):

### Get code
```sh
$ clone git@github.com:cldershem/pinkhatbeard.com.git
$ cd pinkhatbeard.com
```

setup virtualenv
```sh
sudo apt-get install virtualenv virtualenvwrapper

# Py2.7
mkvirtualenv pinkhatbeard.com

# Py3
mkvirtualenv --python=/usr/bin/python3 pinkhatbeard.com
```

### Install dependencies
```sh
# Py2.7
pip install -r requirements.txt

# Py3
pip3 install -r requirements3.txt
```

### Settings
```
$ cp secrets.py.example secrets.py
```

Edit `secrets.py` as indicated in the file.  For testing purposes you can
probably get away without editing anything, but a `SECRET_KEY` is suggested.

### Running
To run a development machine:

```sh
$ python manage.py run
```

A dev server will be running on `localhost:5000`.  By going to the address in
your browser you should be able to view a working version of the site. If you'd
like to make the application available to your local network:

```sh
$ python manage.py run_on_network
```

## LICENSE
See [`TOPMATTER.md`](https://github.com/cldershem/pinkhatbeard.com/blob/master/TOPMATTER.md#license)
## COPYRIGHT
See [`TOPMATTER.md`](https://github.com/cldershem/pinkhatbeard.com/blob/master/TOPMATTER.md#copyright)
## CONTRIBUTING
See [`TOPMATTER.md`](https://github.com/cldershem/pinkhatbeard.com/blob/master/TOPMATTER.md#contributing)
