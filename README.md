# SI507_Project3_zinniak

The **SI507_Project3.py** is a Flask application for a movie database. The application allows a user to add movies, movie genres, directors, and distributors to the database using URL's and shows a list of all movies in the database along with their details.

## Flask Routes
There are 6 routes in the Flask application:
1. `/`
* This route is for the home page that shows the number of movies in the database.
2. `/new/director/<name>/<home>/<dob>/<dod>`
* This route adds a director and their home town, date of birth, and data of death to the database in a director table. If the director already exists, it displays a message accordingly.
3. `/new/genre/<name>`
* This route adds a genre to the database in a genre table. If the genre already exists, it displays a message accordingly.
4. `/new/distributor/<name>`
* This route adds a distributor to the database in a distributor table. If the distributor already exists, it displays a message accordingly.
5. `/new/movie/<title>/<mpaa>/<genre>/<director>/<distributor>`
* This route creates a movie in the database. It checks to see if the movie title already exists, if it does not, it creates the movie. It also checks to see if the director, distributor, and genre already exist. If they do not, it creates them and adds them to their respective tables.
6. `/all_movies` 
* This route shows a list of all movies along with their MPAA rating, director, and distributor.

## How to Run the Flask Application
1. Run the command prompt and go into the directory that has the **SI507_project3.py** file.
2. Once in the correct directory, type the following in the command prompt: `python SI507_project3.py runserver`
3. The application will begin running, open up a tab in a web-browser and type the following in the URL bar: `127.0.0.1:5000`
  This will route to the home page and will display the number of movies in the movie database.

**Refer to the requirements.txt file to see what dependencies you need to install to run the application! To install the requirements, type the following in the command prompt:** `pip install -r requirements`
