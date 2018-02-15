from flask import render_template, request
from app import app
from app.forms import RegistrationForm


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = str(form.email).split("value")[-1].split('"')[1]
        text = str(form.text).split("value")[-1].split('"')[1]
        data = {email: text}
        with open("text.txt","a") as handle:
            handle.write(str(data) +';\n')
        return render_template('index.html')
    return render_template('base.html', title='Register', form=form)