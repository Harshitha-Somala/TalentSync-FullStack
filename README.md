# TalentSync-FullStack
Integrates with PostgreSQL database and fetches Job listings

## Prerequisites
- Follow the link below for the SQL setup to create data tables in database before working with API
- DDL and DML commands are written in SQL_setup folder under  ```ddl.sql`` and ```dml.sql``` files respectively.
https://github.com/Harshitha-Somala/TalentSync-FullStack/blob/main/SQL_setup/setup_instructions.md

## How to run the API
```python flask_server.py```

App will run under the url - http://127.0.0.1:5000 

## How to run tests
```python -m pytest```

Note: Make sure to keep the API running while running tests since server is not mocked at this point

## Sample requests in PostMan

**Sample GET request**
![Sample_get_request](https://github.com/Harshitha-Somala/TalentSync-FullStack/assets/104232955/5afcb65e-9e30-4ed4-b683-e2e89da5a698)

**Sample POST request**
![Sample_post_request](https://github.com/Harshitha-Somala/TalentSync-FullStack/assets/104232955/e09e09ef-5f6e-4d97-a051-9e6aa5f355f4)
