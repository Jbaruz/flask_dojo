from flask_crud import app
from flask_crud.models.dojo import Dojo
from flask import render_template, flash, session, redirect, request

@app.route('/dojos')
def all_dojos():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template('index.html', all_dojos=all_dojos)

@app.route('/dojos', methods=['GET', 'POST'])
def insert_new_dojo():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        print(F'AQUI--->',request.method)
        data = {
            "name": request.form['name'],
        }
        results=Dojo.insert_dojo(data)
        print(f'result in route', results)
        if results != False:
            return redirect('/dojos')
        else:
            flash('There was an error inserting a new dojo', 'danger')
            return redirect('/dojos')

@app.route('/dojos/<id>')
def ninjas_to_show_by_dojo(id):
        return render_template('/users/dojos_detail.html', user = Dojo.get_by_id(id))
    

@app.route('/ninjas', methods=['GET', 'POST'])
def add_new_ninja():
    print(f'REQUEST TYPE', request.method)
    if request.method == 'GET':
        return render_template('users/addNewNinja.html')

    elif request.method == 'POST':
        print(F'AQUI--->',request.method)
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "Age": request.form['age']
        }
        results=Ninja.insert_user(data)
        print(f'result in route', results)
        if results != False:
            return redirect('/ninjas')
        else:
            flash('There was an error inserting a new user', 'danger')
            return redirect('/dojos')