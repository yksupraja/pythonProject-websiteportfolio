from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    from_email = request.form.get('from_email')
    to_email = request.form.get('to_email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Send email using SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'supraja2d@gmail.com'
    smtp_password = 'pndsmcfwifbnbhyv'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)

            email_body = f"Name: {name}\nFrom: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{message}"

            server.sendmail(from_email, to_email, email_body)

        return 'Email sent successfully'
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True,port=8000)

