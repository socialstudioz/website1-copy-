from flask import Flask, render_template, request, redirect
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_url_path='/static')
API_KEY = os.getenv("WEB3FORMS_API_KEY")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/facility')
def facility():
    return render_template('facility.html')

@app.route('/room')
def rooms():
    return render_template('rooms.html')

@app.route('/about')
def about():
    return render_template('about.html')

# 👇 This handles the form submission securely
@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "access_key": API_KEY,
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "phone": request.form.get("phone"),
        "message": request.form.get("message")
    }

    print(f"Data being sent: {data}")

    try:
        response = requests.post("https://api.web3forms.com/submit", data=data)

        # Debugging: print response
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")

        # Checking if the response contains the success HTML message
        if "Form submitted successfully!" in response.text:
            return redirect("/")  # Redirect to home page after success
        else:
            print("❌ Web3Forms API error or unexpected response:", response.text)
            return redirect("/error")  # Redirect to error page if not successful

    except requests.exceptions.RequestException as e:
        print("❌ Network error:", e)
        return redirect("/error")  # Redirect to error page in case of network issues

@app.route('/success')
def success():
    return "✅ Message sent successfully!"

@app.route('/error')
def error():
    return "❌ Message failed to send. Try again later."

if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)