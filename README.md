# Wayfarer

## About

This application is designed to host a travel community, where users can share tips, tricks, and pictures about destinations across the globe.  Users can make their own profiles, add friends, and comment on one another's posts.

## Contents

  1. [Setup](#Setup)
  1. [Usage](#Usage)
  1. [Example of Use](#Example-of-Use)
  1. [Roadmap](#Roadmap)
  1. [Development](#Development)
  1. [Math](#Math)
  1. [License](#License)
  1. [Notes](#Notes)

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
1. Run the application `$ python3 manage.py runserver`
1. View the app in your browser at `http://localhost:8000/`
1. Make an account to access features*

*Note: if Postgres is not yet installed, you will need to run:

`$ brew install postgres`
`$ brew tap homebrew/services`*
`$ brew services start postgresql`

*If homebrew is not installed, you may download it here:
https://docs.brew.sh/Installation


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


1. Create a color using the HTS sliders
1. Click "convert" to convert into hex values
1. OR, click "Save Color" to start a palette
1. Keep adding more colors!
1. Re-order colors in your palette with the "+" & "-" knobs
1. Delete a color with the "X"
1. Press "Hex" to convert everything and start a new palette
1. Confirmation before delete
1. Slug URLs
1. Relative published dates for posts
    
## Examples-of-Use

- [screenshots]

## Roadmap -- pending features

- advanced error handling & data validation
- fix welcome email bug
- make city carousel interactive
- add "default" profile photos
- add metrics for your and your friends' posts
- permissions to only edit one's own comments

## Development

To help with a bug or add functionality, do this:

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
The initial code for this project was contributed via collaboration between JDeliso, dtklumpp and ricksubel, as part of a project for General Assembly.   
