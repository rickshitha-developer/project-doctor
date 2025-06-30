
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Doctoe e-managemnet website/index.html')

@app.route('/services.html')
def services():
    return render_template('Doctoe e-managemnet website/services.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        # Get data from form
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        gender = request.form.get('gender')
        service = request.form.get('service')
        date = request.form.get('date')
        time = request.form.get('time')
        notes = request.form.get('notes')


        # Optional: Save to database or send email

        message = f"Thank you {name}, your appointment for {service} on {date} at {time} has been received. We will contact you at {email}."
        return render_template("Doctoe e-managemnet website/confirmation.html", message=message)
    
    # Fallback to show form
    return render_template("Doctoe e-managemnet website/appointment.html")

@app.route('/login')
def login():
    return render_template('Doctoe e-managemnet website/login.html')

@app.route('/register')
def register():
    return render_template('Doctoe e-managemnet website/register.html')

@app.route('/about')
def about():
    return render_template('Doctoe e-managemnet website/about.html')

    
# ✅ Contact Form Submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = f"Thank you, {name}! Your message has been received. We'll respond to {email} shortly."
        return render_template('Doctoe e-managemnet website/confirmation.html', message=message)

    # GET request — just show the contact form page
    return render_template('Doctoe e-managemnet website/contact.html')



if __name__ == '__main__':
    app.run(debug=True)
