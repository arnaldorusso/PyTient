from flask import render_template, redirect, url_for, jsonify, request
from models import Register_patient
from forms import PatientForm
from pytient_app import app, db
import datetime

@app.route("/")
def index():
    cadastros = Register_patient.query.all()
    form = PatientForm()
    return render_template('index.html', form=form)  # , cadastro=cadastros)

@app.route("/autocomplete",methods=['GET'])
def autocomplete():
    pacientes = Register_patient.query.all()
    NAMES = [p.nome for p in pacientes]
    search = request.args.get('term')
    app.logger.debug(search)
    return jsonify(json_list=NAMES)

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



from flask import jsonify

NAMES=["abc","abcd","abcde","abcdef"]

@app.route('/autocomplete',methods=['GET'])
def autocomplete():
    search = request.args.get('term')

    app.logger.debug(search)
    return jsonify(json_list=NAMES)
