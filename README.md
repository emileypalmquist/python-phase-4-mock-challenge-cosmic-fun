# Flask Mock Challenge - Cosmic Travel

It is the year 2100 and you run an interplanetary space travel agency. You are building a website to book scientists on missions to other planets.

In this repo, there is a Flask application with some features built out. There
is also a fully built React frontend application, so you can test if your API is
working (don't be afraid to use Postman as well).

Your job is to build out the Flask API to add the functionality described in the
deliverables below.

This project is separated into two applications:

- A React frontend, in the `client` directory.
- A Flask backend, in the `server` directory.

All of the features for the React frontend are built out, so you do not need to make any changes there.

---

## Frontend Setup

Let's take a quick tour of what we have so far.

To get started, `cd` into the `client` directory. Then run:

```console
$ npm install
$ npm start
```

Then visit [http://localhost:4000](http://localhost:4000) in the browser to get a sense of the application.

You are not being assessed on React, and you don't have to update any of the React
code; the frontend code is available just so that you can test out the behavior
of your API in a realistic setting.

---

## Backend Setup

In another terminal, run `pipenv install; pipenv shell` to install the
dependencies and enter your virtual environment, then `cd` into the `server`
directory to start running your Python code.

In this directory, you're given a bare-bones template for a Flask API
application. It should look familiar to other Flask labs you've seen and has
all the code set up so you can focus on building out your model and API routes (unless you would prefer to include flask-restful).

You'll be responsible for:

- Creating the models and migrations.
- Setting up the necessary routes to handle requests.
- Performing CRUD actions and validations with SQLAlchemy.
- Sending the necessary JSON data in the responses.

## Instructions

You can run your Flask server from the
`server/` directory with:

```console
$ python app.py
```

## If you would prefer to include Flask Restful complete the following otherwise skip to Models section

This application is using vanilla Flask. If you would like to use flask-restful you can. To setup Flask-restful complete the following steps:

- in the main install flask-restful:

```console
$ pipenv install flask-restful
```

- in the `app.py` file import Api and Resource from flask-restful

```python
from flask_restful import Api, Resource
```

- connect flask-restful to you app

```python
api = Api(app)
```

- remove the routes index route currently setup in `app.py`
- create classes that inherit `Resource` (imported from flask-restful)
- add resources to your api

## Models

It is your job to build out Planet, Scientist, and Mission models so that scientists can book their missions. **In a given mission, one scientist will visit one planet**. Over their careers, **scientists will visit many planets** and **planets will be visited by many scientists**.

You need to create the following relationships:

- A `Scientist` has many `Missions`, and has many `Planet`s through `Mission`s
- An `Planet` has many `Missions`, and has many `Scientist`s through `Mission`s
- A `Mission` belongs to a `Scientist` and belongs to a `Planet`

Start by creating the models and migrations for the following database tables:

![cosmic_erd](https://curriculum-content.s3.amazonaws.com/phase-4/mock-challenge-cosmic-challenge/cosmic_erd.png)

## Validations

Add validations to the `Scientist` model:

- must have a `name`, and a `field_of_study`
- `name`s must be unique

Add validations to the `Mission` model:

- must have a `name`, a `scientist` and a `planet`
- a `scientist` cannot join the same `mission` twice

After creating the model and migrations, run the migrations and use the provided
`seed.py` file to seed the database:

```console
$ flask db migrate -m'your message'
$ flask db upgrade
$ python seed.py
```

If you run into errors with the migrate or upgrade try:

- deleting the migrations folder and the database
- run the following command to restart the db setup

```console
$ flask db init
```

- try the migrate and upgrade commands again

### Routes

Set up the following routes. Make sure to return JSON data in the format
specified along with the appropriate HTTP verb.

### GET /scientists

Return JSON data in the format below. **Note**: you should return a JSON
response in this format, without any additional nested data related to each
scientist.

```json
[
  {
    "id": 1,
    "name": "Mel T. Valent",
    "field_of_study": "xenobiology",
    "avatar": "https://robohash.org/mel_t_valent?set=set5"
  },
  {
    "id": 2,
    "name": "P. Legrange",
    "field_of_study": "orbital mechanics",
    "avatar": "https://robohash.org/p_legrange?set=set5"
  }
]
```

### GET /scientists/:id

If the `Scientist` exists, return JSON data in the format below. **Note**: you will
need to serialize the data for this response differently than for the
`GET /scientists` route. Make sure to include an array of missions for each
scientist.

```json
{
  "id": 1,
  "name": "Mel T. Valent",
  "field_of_study": "xenobiology",
  "avatar": "https://robohash.org/mel_t_valent?set=set5",
  "planets": [
    {
      "id": 1,
      "name": "TauCeti E",
      "distance_from_earth": "12 light years",
      "nearest_star": "TauCeti",
      "image": "planet3"
    },
    {
      "id": 2,
      "name": "Maxxor",
      "distance_from_earth": "9 parsecs",
      "nearest_star": "Canus Minor",
      "image": "planet7"
    }
  ]
}
```

If the `Scientist` does not exist, return the following JSON data, along with
the appropriate HTTP status code:

```json
{
  "error": "Scientist not found"
}
```

### POST /scientists

This route should create a new `Scientist`. It should accept an object with the
following properties in the body of the request:

```json
{
  "name": "Evan T'Horizon",
  "field_of_study": "astronavigation",
  "avatar": "https://robohash.org/evan_thorizon?set=set5"
}
```

If the `Scientist` is created successfully, send back a response with the new
`Scientist`:

```json
{
  "id": 3,
  "name": "Evan T'Horizon",
  "field_of_study": "astronavigation",
  "avatar": "https://robohash.org/evan_thorizon?set=set5"
}
```

If the `Scientist` is **not** created successfully, return the following JSON data,
along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```

### PATCH /scientists/:id

This route should update an existing `Scientist`. It should accept an object with one or more of the
following properties in the body of the request:

```json
{
  "name": "Bevan T'Horizon",
  "field_of_study": "warp drive tech",
  "avatar": "https://robohash.org/bevan_thorizon?set=set5"
}
```

If the `Scientist` is updated successfully, send back a response with the updated
`Scientist` and a 202 status code:

```json
{
  "id": 2,
  "name": "Bevan T'Horizon",
  "field_of_study": "warp drive tech",
  "avatar": "https://robohash.org/bevan_thorizon?set=set5"
}
```

If the `Scientist` is **not** updated successfully, return the following JSON data,
along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```

OR, given an invalid ID, the appropriate HTTP status code, and the following JSON:

```json
{
  "error": "Scientist not found"
}
```

### DELETE /scientists/:id

If the `Scientist` exists, it should be removed from the database, along with
any `Mission`s that are associated with it (a `Mission` belongs
to an `Scientist`, so you need to delete the `Mission`s before the
`Scientist` can be deleted. If you are stuck on this check the resources at the bottom of this file.).

After deleting the `Scientist`, return an _empty_ response body, along with the
appropriate HTTP status code.

If the `Scientist` does not exist, return the following JSON data, along with
the appropriate HTTP status code:

```json
{
  "error": "Scientist not found"
}
```

### GET /planets

Return JSON data in the format below. **Note**: you should return a JSON
response in this format, without any additional nested data related to each
planet.

```json
[
  {
    "id": 1,
    "name": "TauCeti E",
    "distance_from_earth": "12 light years",
    "nearest_star": "TauCeti",
    "image": "planet3"
  },
  {
    "id": 2,
    "name": "Maxxor",
    "distance_from_earth": "9 parsecs",
    "nearest_star": "Canus Minor",
    "image": "planet7"
  }
]
```

### POST /missions

This route should create a new `Mission`. It should accept an object with the
following properties in the body of the request:

```json
{
  "name": "Project Terraform",
  "scientist_id": 1,
  "planet_id": 2
}
```

If the `Mission` is created successfully, send back a response with the `planet` associated with the new `Mission` (contrary to convention, which normally dictates the response would include data about the _mission_ that was created):

```json
{
  "id": 2,
  "name": "Maxxor",
  "distance_from_earth": "9 parsecs",
  "nearest_star": "Canus Minor",
  "image": "planet7"
}
```

If the `Mission` is **not** created successfully, return the following JSON data,
along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```

## Resources

- [Flask - Pallets](https://flask.palletsprojects.com/en/2.2.x/)
- [Cross-Origin Resource Sharing - Mozilla][cors mdn]
- [Flask-CORS][flask-cors]
- [flask.json.jsonify Example Code - Full Stack Python](https://www.fullstackpython.com/flask-json-jsonify-examples.html)
- [SQLAlchemy-serializer - PyPI](https://pypi.org/project/SQLAlchemy-serializer/)
- [Many-to-Many Assocation](https://www.youtube.com/watch?v=IlkVu_LWGys)
- [Deleting Related Objects](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_deleting_related_objects.htm)

[cors mdn]: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
[flask-cors]: https://flask-cors.readthedocs.io/en/latest/
