# How to setup project

1. Clone repository

```git pull```

2. Install Python3.8

3. Create virtual environment using `virtualenv`
```
$ python3 -m pip install --upgrade pip
$ pip3 install --upgrade setuptools
$ pip3 install virtualenv
$ virtualenv -p /usr/bin/python3.8 venv
$ source venv/bin/activate
```

4. Install requirements

```$ pip install -r requirements.txt```

5. Run project

```$ gunicorn -w 4 'main:app'```