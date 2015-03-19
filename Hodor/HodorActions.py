"""List of actions that Hodor can perform.

Currently, three moods are defined:

- happy
- neutral
- sad

Adding additional moods will require adjusting Hodor's class.

Additionally, each mood is defined with a weight, which controls how
often that action will occur. Weights must be integers.
"""

actions = {
    'happy': [
        {
            'weight': 50,
            'action': {
                'type': 'privmsg',
                'value': 'Hodor!'
            }
        },
        {
            'weight': 25,
            'action': {
                'type': 'privmsg',
                'value': 'Hodor! Hodor!',
            }
        },
        {
            'weight': 2,
            'action': {
                'type': 'privmsg',
                'value': 'Hodor! Hodor! Hodor! Hodor! Hodor! Hodor! Hodor!'
            }
        },
        {
            'weight': 10,
            'action': {
                'type': 'action',
                'value': 'grins, mouth gaping'
            }
        },
        {
            'weight': 5,
            'action': {
                'type': 'action',
                'value': 'smiles'
            }
        },
        {
            'weight': 5,
            'action': {
                'type': 'action',
                'value': 'groans'
            }
        }
    ],
    'neutral': [
        {
            'weight': 50,
            'action': {
                'type': 'privmsg',
                'value': 'Hodor?'
            }
        },
        {
            'weight': 30,
            'action': {
                'type': 'action',
                'value': 'stares blankly'
            }
        },
        {
            'weight': 30,
            'action': {
                'type': 'action',
                'value': 'scratches his head'
            }
        }
    ],
    'sad': [
        {
            'weight': 25,
            'action': {
                'type': 'privmsg',
                'value': 'Hodor.'
            }
        },
        {
            'weight': 15,
            'action': {
                'type': 'action',
                'value': 'weeps openly'
            }
        },
        {
            'weight': 15,
            'action': {
                'type': 'privmsg',
                'value': 'Hodor:('
            }
        },
        {
            'weight': 5,
            'action': {
                'type': 'action',
                'value': 'stares blankly'
            }
        },
        {
            'weight': 5,
            'action': {
                'type': 'action',
                'value': 'staggers back'
            }
        },
        {
            'weight': 5,
            'action': {
                'type': 'action',
                'value': 'sobs'
            }
        }
    ]
}
