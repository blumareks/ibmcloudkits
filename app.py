import psycopg2
from flask import Flask, request, jsonify, make_response
from os import environ
import sendgrid
from sendgrid.helpers.mail import *
from python_http_client.exceptions import HTTPError


msg = "hello world"
print(msg)
print("i'm in container, eh!")
print(" call youraddress:yourport/test, youraddress:yourport/mailtest or youraddress:yourport/dbtest to test the connection ")

#getting env variables 
HOST = environ.get("HOST")
PORT=environ.get("PORT")
USER= environ.get("USER")
PASSWORD=environ.get("PASSWORD")
SSLMODE=environ.get("SSLMODE")
SSLROOTCERT=environ.get("SSLROOTCERT")
DATABASE=environ.get("DATABASE")
POSTGRESS=environ.get("POSTGRESS")
SENDGRID_API_KEY=environ.get("SENDGRID_API_KEY")
SENDGRID_FROM=environ.get("SENDGRID_FROM")
app = Flask(__name__)


#create a test route
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)




# RESTAPI call /mailtest?email=mytest@roboticsinventions.com
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python


@app.route('/mailtest', methods=['GET'])
def send_testemail():
    from_email = Email(SENDGRID_FROM)
    toEmailFromUrl = request.args.get('email', default = 'test@roboticsinventions.com', type = str)
    to_email = To(toEmailFromUrl)
    subject = "Sending with SendGrid in IBM Cloud is Fun"
    content = Content("text/plain", "and easy to do anywhere, check repo here: github.com/blumareks/ibmcloudkits ")
    mail = Mail(from_email, to_email, subject, content)
    
    print(mail)
    try:
        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        print('obtained sg client')
        response = sg.client.mail.send.post(request_body=mail.get())
        #response = sg.send(message=message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except SendGridException as e:
        print("Unable to connect to sendgrid")
        print(e.message)
        return make_response(jsonify({'message': 'error getting connecting to sendgrid'}), 500)
    return make_response(jsonify({'message_sent to: ':toEmailFromUrl}), 200)    
# END SENDGRID


# RESTAPI call /dbtest
# get all dbs
@app.route('/dbtest', methods=['GET'])
def get_dbs():
    try:
        conn = psycopg2.connect(
        host=HOST,
        port= PORT,
        user=USER,
        password=PASSWORD,
        sslmode=SSLMODE,
        sslrootcert=SSLROOTCERT,
        database=DATABASE)
    except: 
        print("Unable to connect to database")
        return make_response(jsonify({'message': 'error getting connecting to DB'}), 500)

    cur = conn.cursor()
    cur.execute("SELECT datname FROM pg_database")
    rows = cur.fetchall()

    print("List of databases:")
    myDatabases="List of databases:"
    for row in rows:
        print("  ",row[0])
        myDatabases=myDatabases+"  ",row[0]
    return make_response(jsonify([myDatabases.json()]), 200)
# END POSTGRESQL


