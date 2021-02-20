# Wayfarer

This application is designed to host a travel community, where users can share tips, tricks, and pictures about destinations across the globe.  Users can make their own profiles, add friends, and comment on one another's posts (and comments).

Travel applications as they stand (at the time of writing) are either heavily commerce-focused, or have a top-down model of content creation.  We attempt to democratize this with a bare-bones build designed to run quickly with no extraneous features or ads.

## example-of-use

![Screen Shot 2021-02-05 at 12 15 43 AM](https://user-images.githubusercontent.com/65556316/107082185-cff1a000-67c1-11eb-88a4-030450d7bbc6.png)


## Contents

  1. [Requirements](#Requirements)
  1. [Usage](#Usage)
  1. [Features](#Features)
  1. [Roadmap](#Roadmap)
  1. [Development](#Development)
  1. [License](#License)
  1. [Notes](#Notes)
  1. [Screenshots](#Screenshots)


## Requirements

- Django 3.1.2
- Pillow 7.2.0
- psycopg2-binary 2.8.6
- sqlparse 0.4.0
- pytz 2020.1
- asgiref 3.2.10
- Postgres 12.4

## Usage

To clone and run this app, you'll need [Git](https://git-scm.com) installed on your computer.  From the command line:

1. Clone this repo (`https://github.com/dtklumpp/wayfarer-djr`)
1. Enter the repository `$ cd wayfarer-djr`
1. Enter the virtual environment `$ source .env/bin/activate`
1. Exit .env at any time with `$ deactivate`
1. Install dependencies with `$ pip3 install -r requirements.txt`
1. Run the application `$ python3 manage.py runserver`
1. View the app in your browser at `http://localhost:8000/`
1. Make an account to access features*

*Note: if Postgres is not yet installed, you will need to run:

```
$ brew install postgres
$ brew tap homebrew/services*
$ brew services start postgresql
```

*If homebrew is not installed, you may download it here:

https://docs.brew.sh/Installation

To seed the database, run these commands:

```
$ createdb wayfarerdb-v3
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
```

...with your superuser credentials you may then log in to the Django admin panel




## Features

1. Create an account and log in
1. Create a city or location
1. Add pictures, a description, and basic info
1. Post information about a city
1. View other users posts
1. Make comments
1. Edit or Delete cities, posts, users, comments
1. Select a city from the interactive map
1. Basic data validation and error handling
1. Send a welcome email after acccount creation
    


## Roadmap -- pending features

- advanced error handling & data validation
- fix welcome email bug
- make city carousel interactive
- add "default" profile photos
- add metrics for your and your friends' posts
- permissions to only edit one's own comments

## Development

To contribute to this project, follow these steps:

- Fork this repo
- Make a branch (`git checkout -b new-feature`)
- Make modifications where necessary
- Add comments corresponding to your changes
- Commit (`git commit -m 'explanation'`)
- Push up (`git push origin new-feature`)
- Make a Pull Request 


## License

MIT ©


## Notes
The initial code for this project was contributed via collaboration between JDeliso, dtklumpp and ricksubel

---
---

## Screenshots

Splash Page

![Screen Shot 2021-02-05 at 12 15 43 AM](https://user-images.githubusercontent.com/65556316/107082185-cff1a000-67c1-11eb-88a4-030450d7bbc6.png)

Map View

![Screen Shot 2021-02-05 at 12 16 23 AM](https://user-images.githubusercontent.com/65556316/107082223-dbdd6200-67c1-11eb-9618-07fb5b4f6444.png)

City View

![Screen Shot 2021-02-05 at 12 16 03 AM](https://user-images.githubusercontent.com/65556316/107082244-e39d0680-67c1-11eb-865a-25d638d55244.png)

Modals

<img width="1440" alt="Screen Shot 2021-02-05 at 5 11 57 PM" src="https://user-images.githubusercontent.com/65556316/107094683-72ffe500-67d5-11eb-85c4-e874052310dd.png">
