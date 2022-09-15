from flask_crud import app
from flask_crud.models.dojo import Dojo
from flask_crud.models.ninja import Ninja
from flask import render_template, flash, session, redirect, request

@app.route('/ninjas', methods= ['GET', 'POST'])
def ninjas():
    return render_template('/users/addNewNinja.html', ninjas=Ninja.get_all, dojos=Dojo.get_all())

@app.route('/ninjas/process', methods=['POST'])
def process_new_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id'],
    }
    new_ninja = Ninja.add_ninja(data)
    print("aqui quiero ver------>", data)
    if new_ninja != False:
        return redirect(f"/dojos/{request.form['dojo_id']}")
    flash('Failed to create Ninja', 'danger')
    return redirect('/dojos')


