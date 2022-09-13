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

    
