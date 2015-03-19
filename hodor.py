"""rtmbot plugin for slack; does hodoring.

Listen for mentions of Hodor's name in channels and reply with a message.
Messages are pre-defined from a basic module import and classified by mood.
The 'mood' of reply is determined by comparing the content of the triggering
message against a library of words and human interpreted intent scoring. After
mood assignment, a message is chosen based on a dropo-type selection process
that allows for weighting of responses."""

from Hodor.Hodor import Hodor
import random
import time

crontable = []
outputs = []

def process_message(data):
    if 'text' in data:
        if 'hodor' in data['text'].lower():
            hodor = Hodor(data['text'], )
            action_to_take = hodor.act()
            time.sleep(random.random() * 5)
            if action_to_take['type'] == 'action':
                output_string = '*' + action_to_take['value'] + '*'
            else:
                output_string = action_to_take['value']
            outputs.append([data['channel'], output_string])
