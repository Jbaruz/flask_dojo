from flask_crud import app
from flask_crud.models.dojo import Dojo
from flask_crud.models.ninja import Ninja
from flask import render_template, flash, session, redirect, request

@app.route('/ninjas', methods= ['GET', 'POST'])
def ninjas():
    return render_template('/users/addNewNinja.html', ninjas=Ninja.get_all())


@app.route('/ninjas/<id>', methods=['GET'])
def ninjas_detalle(id):
    
    return render_template('users/ninjas_detalle.html', ninjas = Ninja.get_by_id(id), dojos=Dojo.get_all())