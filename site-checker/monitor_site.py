from requests import get
from twilio.rest import TwilioRestClient
from time import sleep
import json

json_data=open("config.json").read()
config = json.loads(json_data)
twilio_config = config["twilio"]
twilio_client = TwilioRestClient(twilio_config["account"], twilio_config["token"])
website = config["website"]

initial = get(website['url']).text
while 1:
	current = get(website['url']).text
	if (current != initial):
		initial = current
		twilio_client.messages.create(to=twilio_config["to"], from_=twilio_config["from"],
                                 body=twilio_config["body"])
	sleep(website["frequency_in_sec"])