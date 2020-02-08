# Instructions:

- Pull down the project: `git clone https://github.com/ilgor/eastridge_interview.git`
- Go inside the project: `cd eastridge_interview`
- Activate Virtual Environment: `pipenv shell`
- Install Dependencies: `pipenv install`
- To populate initial DB run the following: `python build_database.py`
- Run the app: `python app.py`


# API info
- GET all invoices: `/`
- POST invoice with invoice items: `/`, Header: `["key":"Content-Type","value":"application/json"]`, Body(raw): `{"client_name":"Eastridge","invoice_items":[{"units":1,"description":"Some cool product #1","amount":19.99},{"units":2,"description":"Some cool product #2","amount":29.99}]}`

- GET single invoice based on `id`: `/id`
- DELETE single invoice based on `id`: `/id`

- GET invoices based on date: TODO
- GET 1 invoice based on client: `/client_name={name}` (TODO)
- DELETE single invoice based on `/client_name={name}` (TODO)