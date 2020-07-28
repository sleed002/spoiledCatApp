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
            msg.body("Treats deployed successfully.   Would you like to give Milo more treats? Yes/No")
            msg.media("https://res.cloudinary.com/fotobooth/image/upload/milo.jpg")
        except:
            print("Treats did not deploy. Try again? Yes/No")
            msg.body("Deploy failed.")
    elif body == 'pic' or body == "photo":
        call(["python", "runCamera.py"])
        msg.body("Here is a picture of Milo. Would you like to give Milo treats? Yes/No")
        msg.media("https://res.cloudinary.com/fotobooth/image/upload/milo.jpg")
    elif body == 'no':
        msg.body("Milo is sad but understands.")
    else:
        msg.body("Welcome to Milo's treat dispenser app. Text 'Treats' to give Milo treats. Text 'Pic' or 'Photo' to take a picture")

    return str(resp) 

if __name__ == "__main__":
    app.run(debug=True)