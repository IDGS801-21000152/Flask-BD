
from config import DevelopmentConfig

from flask import Flask, redirect, render_template, request, url_for
from flask import flash
from flask import g
from flask_wtf.csrf import CSRFProtect
import forms
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def main():
    return render_template("layout.html")

@app.route("/registrar_alumno", methods=["GET", "POST"])
def registrarAlumno():
    create_form = forms.UserForm(request.form)
    
    if request.method == "POST":
        alumnos = Alumnos(
            nombre = create_form.nombre.data,
            primerApellido = create_form.primerApellido.data,
            segundoApellido = create_form.segundoApellido.data,
            correo = create_form.correo.data
        )
        db.session.add(alumnos)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    
    return render_template('registrar_alumno.html', form=create_form)

@app.route("/ABC_Completo", methods=["GET", "POST"])
def ABCompleto() :
    form_alumno = forms.UserForm(request.form)
    alumnos = Alumnos.query.all()
    
    return render_template("ABC_Completo.html", alumnos = alumnos)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    
    if request.method == 'GET':
        id = request.args.get('id')
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alumno.nombre
        create_form.primerApellido.data = alumno.primerApellido
        create_form.segundoApellido.data = alumno.segundoApellido
        create_form.correo.data = alumno.correo
    
    if request.method == 'POST':
        id = create_form.id.data
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alumno.nombre = create_form.nombre.data
        alumno.primerApellido = create_form.primerApellido.data
        alumno.segundoApellido = create_form.segundoApellido.data
        alumno.correo = create_form.correo.data
        
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    
    
    return render_template('modificar.html', form=create_form)
    
@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    
    if request.method == 'GET':
        id = request.args.get('id')
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alumno.nombre
        create_form.primerApellido.data = alumno.primerApellido
        create_form.segundoApellido.data = alumno.segundoApellido
        create_form.correo.data = alumno.correo
    
    if request.method == 'POST':
        id = create_form.id.data
        alumno = Alumnos.query.get(id)
        
        db.session.delete(alumno)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    
    
    return render_template('eliminar.html', form=create_form)
    
    
if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.run()