from flask import render_template, flash, request, redirect, url_for
from app import app
from app.models.IA import *

@app.route("/", methods=['GET', 'POST'])
def index():
    ia_response = None

    if request.method == 'POST':
        texto = request.form['InputEntrada']
    
        response = chat.send_message(texto)
        ia_response = response.text

    return render_template('index.html', ia_response=ia_response)
