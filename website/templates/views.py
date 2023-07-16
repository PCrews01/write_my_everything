from flask import Blueprint, render_template, request, flash, escape, url_for, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login  import login_user, login_required, logout_user, current_user
from .models import *
from website import db

import os
import openai
import time
import threading

views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    print(f"oooop {session['user']}")
    if request.method == 'POST':
        openai.api_key = os.getenv('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')
        title = request.form.get('title')
        topic = request.form.get('topic')
        grade = request.form.get('grade')
        length = request.form.get('length')
        measurement = request.form.get('meass')
            
        essay = Essays(title=title, topic=topic, grade_level=grade, essay_length=length, essay_measurement=measurement)
        
        prompt = 'Can you write a ' + length + ' ' + measurement + ' essay on ' + topic + '. Summarize for ' + grade + '-grade level.'
        def fetchResponse():
            res = openai.Completion.create(
                api_key="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",
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.1,
                max_tokens=4000,
                n=1,
                frequency_penalty=2.0
            )
            r_get = res.get('choices')[0].text
            return r_get
        def displayLoader():
            print("Waiting for this thing to load")
            data = fetchResponse()
            print(data)
            
        thread = threading.Thread(target=displayLoader)
        thread.start()
        while thread.is_alive():
                print("I'm alive")
                loading = False
                status = "loading"
                time.sleep(1)
                return render_template('home.html', prompt=prompt, title=title, completion=fetchResponse(), user=current_user)
        status = "DONE"
        # return render_template('home.html', prompt=prompt, title=title, completion=fetchResponse(), user=current_user)
    return render_template('home.html', user=current_user)

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    users = User.query.get().all()
    return render_template('contact.html')