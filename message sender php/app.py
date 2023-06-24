from flask import Flask, render_template, request
from twilio.rest import Client
import keys

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html', twilio_number=keys.twilio_number)

@app.route('/send', methods=['POST'])
def send_message():
    phone_number = keys.my_phone_number
    twilio_number = keys.twilio_number
    message_body = request.form['message_body']

    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to=phone_number
    )

    return 'Message sent successfully'

if __name__ == '__main__':
    app.run()
