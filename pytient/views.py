from flask import render_template, redirect, url_for
from models import Register_patient
from forms import PatientForm
from pytient_app import app, db
import datetime

@app.route("/")
def index():
    cadastros = Register_patient.query.all()
    form = PatientForm()
    return render_template('index.html', form=form)  # , cadastro=cadastros)

@app.route(u'/new', methods=[u'POST'])
def newpatient():
    form = PatientForm()
    if form.validate_on_submit():
        cadastro = Register_patient(
            form.nome.data,
            form.rg.data,
            form.nascimento.data,
            datetime.datetime.now()
            )
        # form.populate_obj(cadastro)
        db.session.add(cadastro)
        db.session.commit()
    return redirect(url_for('index'))
