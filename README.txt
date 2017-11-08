Pyramid Learning Journal
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

