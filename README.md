# Instructions:

- Pull down the project: `git clone https://github.com/ilgor/eastridge_interview.git`
- Go inside the project: `cd eastridge_interview`
- Activate Virtual Environment: `pipenv shell`
- Install Dependencies: `pipenv install`
- To populate initial DB run the following: `python build_database.py`
- Run the app: `python app.py`


# API info
- GET all invoices: `/`
- GET 1 invoice based on client: `/client_name={name}` (TODO)
- GET invoices based on date: TODO
- POST an invoice TODO