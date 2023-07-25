# FastAPI Example With JWT Docker And PostgreSQL

The task is to create a simple blog application using latest `FastAPI` framework where users can login, sign up, create/delete posts. Staff members can see the list of signed-up users and delete users. Also `JWT` autherntication. 

## Step
- FastApi (Python 3.10 or above)
- Use the PostgreSQL database
- JWT for authentication
- User verification and SMTP configuration
- Docker to run the project

## Build with
* [Python v3.10](https://www.python.org/)
* [FastAPI v0.100.0](https://fastapi.tiangolo.com)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [JWT Auth](https://jwt.io/)

### Dependency
```sh
alembic==1.11.1
email-validator==2.0.0.post2
fastapi==0.100.0
fastapi-pagination==0.12.6
passlib==1.7.4
psycopg2==2.9.6
pydantic==2.0.3
PyJWT==2.8.0
SQLAlchemy==2.0.19
uvicorn==0.23.1
python-dotenv==1.0.0
bcrypt==4.0.1
pydantic-settings==2.0.2
```

## Installation

You can easily set up the project by following the steps below. In that case, `Docker` and `Docker Compose` are required.

1. Clone the repo
   ```sh
   git clone git@github.com:farjanul/fastapi-example-with-jwt-docker-postgresql.git
   ```   
2. Create the `.env` file copying from `.env.example` and update these values for both projects.
3. Run the project.
4. Import collection of API into (Postman) from doc directory. [Here](https://github.com/farjanul/fastapi-example-with-jwt-docker-postgresql/blob/master/doc/FastAPI%20Demo.postman_collection.json)
5. Or follow the swagger API documentation `http://127.0.0.1:8000/docs`

### Run
  ```sh
  docker-compose up --build -d
  ```

## Let's Enjoy
```
http://127.0.0.1:8000
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Developer
Follow me on - [@LinkedIn](https://www.linkedin.com/in/farjanuln/)

😊 Happy Coding 😊
