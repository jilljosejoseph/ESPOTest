# ESPOTest
---

*This test is just to show comfort levels with basic Django, Docker, and databases*

## Step 0:
Make sure you have the following installed:
- Python
- Docker
- docker-compose (if not on Windows)

## Step 1:
Fork this repository and clone to your local machine.

## Step 2:
 - Start a local instance of the docker image to create a development environment by running the following command:
```
docker-compose up
```

 - Run the following commands to put models in the database:
```
python manage.py migrate
python manage.py makemigrations inventory_management
python manage.py migrate
```

## Step 3:
Create a webpage where you can view data and insert new data into the database.

To do this, you can modify the "home" view in ``inventory_management/views.py``, as well as add any new views as needed.
In the ``inventory_management/templates/home.html``, you will find a blank template HTML file. You can add your data viewing and data input to this file.


---

### Other information
 - The webpage doesn't need to look beautiful but have some sort of user-friendliness
 - Data validation, autocomplete, user authentication, etc. are not required