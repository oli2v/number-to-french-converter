# number-to-french-converter
## About the project
This project is a Flask web application which aims at converting numbers ranging from 0 to 999 999 to French.

## Expected behavior
The user inputs a list of integers comprised within the 0-999999 range and the app should output the list of converted numbers in French.
For example, given the list of integers `1, 2, 3`, it should output `un, deux, trois`.

## Usage
The application is containerized with Docker so you first need to build the image by running the following command: `make build`.
Then simply run `make run` to run the application. It should now be up and running! You can access it via your web browser at the following url: `http://127.0.0.1:5000`.

## Author
[Olivier Valenduc](https://github.com/oli2v)