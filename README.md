# My Gallery

#### This is a beautiful image application that has a variety of images from different categories, 11/05/2019

#### By **Elizabeth Wanjiku Kimita**

## Description
My Gallery is a website that gets to showcase beautiful images from different categories. Users are not only able to view all the images but also search for images based on a specific category. The admin gets to upload the different images and users can share and copy the image links as they please.Images can also be filtered based on their locations.

## BDD Specifications

|    Users Requirements    |                Input              |               Output                     |
| :---------------------:  |   :----------------------------:  |  :------------------------------------:  |
| To view all images       |   Navigate to the home page       | All the images will be displayed         |
|                                                                                                         |
| View image details       |   Click on the image              | image details will be displayed          |
| Search for images in         Input the image category in       images in that category will be          |
| the same category        |    the search bar                 | displayed                                |
| Filter images based      |   navigate to the filter          | Displays images for that location        |
| on location              |   button and select a location    |                                          |
| Copy image Link          |   Click on copy link on the       | Copies the image link path               |
|                          |   image footer                    |                                          |



## Setup/Installation Requirements
* Ensure you have Installed Python3.6
* Clone the My Gallery Repository
* Create and Activate your virtual environment - `python3.6 -m venv --without-pip virtual` && `source virtual/bin/activate`
* Install dependencies - `pip install -r requirements.txt`
* Create a Database - `psql` then `CREATE DATABASE my_gallery`
* Run Migrations - `python3.6 manage.py makemigrations my_gallery` then `python3.6 manage.py migrate`
* Run the App - `python3.6 manage.py runserver`
* Application should open on `localhost:8000` 

## Known Bugs
There are currently no known bugs

## Technologies Used
* Python 3.6
* Bootstrap
* Heroku
* HTML
* Django

## Support and contact details
For more information, questions, or help using the program, get in touch with me on +254 726 047102 or email: kimita.wanjiku@gmail.com.

### License
MIT
Copyright (c) {2019} **Elizabeth Wanjiku Kimita**
  