# Pipenv

```diff
- I used Pipenv for virtual env, please install it on your computer before doing anything
```
If you dont have `Pipenv` please follow the official docs to install [here](https://pypi.org/project/pipenv/)

# Instructions:


- Pull down the project: `git clone https://github.com/ilgor/eastridge_interview.git`
- Go inside the project: `cd eastridge_interview`
- Activate Virtual Environment: `pipenv shell`
- Install Dependencies: `pipenv install`
- To populate initial DB run the following: `python build_database.py`
- Run the app: `python app.py`


# API info
- GET all invoices: `/all`
- GET any combination of Invoices by passing Params. Example: `localhost:5000/all?client_name=Eastridge&amount=19.99&units=5`

- POST invoice with invoice items: `/new`, Header: `["key":"Content-Type","value":"application/json"]`, Body(raw): `{"client_name":"Eastridge","invoice_items":[{"units":1,"description":"Some cool product #1","amount":19.99},{"units":2,"description":"Some cool product #2","amount":29.99}]}`

- GET single invoice based on `id`: `/id`
- DELETE single invoice based on `id`: `/id`

- GET 1 invoice based on client: `/client_name/{name}`
- DELETE single invoice based on `/client_name/{name}`
