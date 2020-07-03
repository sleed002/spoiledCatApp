from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from subprocess import call

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None).lower()

    # Start our TwiML response
    resp = MessagingResponse()
    msg = resp.message()

    # Determine the right reply for this message
    if body == 'yes' or body == "treats":
        msg.body("Milo says 'Thanks for the treats!'")
        # execute program
        try:
            call(["python", "dropTreats.py"])
            msg.body(" Treats deployed successfully.")
        except:
            print("  Treats did not deploy")
            msg.body("Deploy failed.")

    elif body == 'no':
        msg.body("Milo is sad but understands.")
    else:
        msg.body("Welcome to Milo's treat dispenser app. Text 'treats' to give Milo treats or reply 'yes/no'")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)