# pyramid-learning-journal
========================

**Authors** [Han Bao](https://github.com/han8909227) , Darren Haynes
**Deployed Site:*** https://thawing-ocean-94459.herokuapp.com/

Main Libraries & Framwork
- [Pyramid](https://trypyramid.com/)
- [CookieCutter](https://github.com/audreyr/cookiecutter)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)


| Route | Route Name | Description |
| --- | --- | --- |
|`/` | home | Show a list of journals in on the site|
| `/new-entry`| create | Create a new journal (title/body/time required) |
| `/post/{id:\d+}` | detail | Show all contents of a single journal by id |
| `/{id:\d+}/edit-entry` | edit | Edit a specific journal by id |


- Create new virtual environment with python3 and activate it.
```
pyramid_learning_journal $ python3 -m vevn ENV
pyramid_learning_journal $ python3 ENV/bin/activate
```
```
(ENV) pyramid_learning_journal $ pip install -e .[testing]
```

- Create a postgres database
- Export database url as DATABASE_URL in the environment variable
- Initialize the database with the  `initializedb` command
```
    env/bin/initialize_learning_journal_db development.ini
```

To run the project's test
```
    env/bin/pytest
```

To run the project
```
    env/bin/pserve development.ini

```




STEP 2:

=======
__init__.py                  10      7    30%   8-14
data/__init__.py              0      0   100%
data/list_journal.py         14      0   100%
models/__init__.py           24      0   100%
models/meta.py                5      0   100%
models/mymodel.py            12      0   100%
routes.py                     6      0   100%
scripts/__init__.py           0      0   100%
scripts/initializedb.py      31     20    35%   22-25, 29-56
tests.py                     96      0   100%
views/__init__.py             0      0   100%
views/default.py             18      1    94%   25
views/notfound.py             4      2    50%   6-7
-------------------------------------------------------
TOTAL                       220     30    86%

