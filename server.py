from flask_crud import app
from flask_crud.controllers import dojos, ninjas, core
from flask import render_template, redirect



if __name__ == '__main__':
    app.run(debug=True)