from twilio.rest import Client
import os
from configparser import ConfigParser

basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
configPath = os.path.join(basepath, "spoiledCatApp/etc", "config.ini")
config = ConfigParser()
config.read(configPath)

assert os.path.exists(configPath)

ACCOUNT_SID = config.get("twilio", "ACCOUNT_SID")
AUTH_TOKEN = config.get("twilio", "AUTH_TOKEN")
TO_NUMBER = config.get("twilio", "TO_NUMBER"),
FROM_NUMBER = config.get("twilio", "FROM_NUMBER"),

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
to_number=TO_NUMBER,
from_number=FROM_NUMBER,

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to=to_number,
    from_=from_number,
    body="Milo wants treats! Dispense treats? yes/no"
    )

# exec(open("dropTreats.py").read())