"""This is Hodor himself.

"""
import HodorActions
import HodorMoodIndex
import random
import re


class Hodor(object):
    def __init__(self, message):
        self.message = message
        self.interpret_mood()
        self.mood = 'happy'

    def interpret_mood(self):
        mood_score = 0
        for curword in re.sub("[^\w]", " ",  self.message).split():
            try:
                mood_score += HodorMoodIndex.mood_index[curword]
            except:
                pass
        if mood_score >= 2:
            self.mood = 'happy'
        elif mood_score <= -2:
            self.mood = 'sad'
        else:
            self.mood = 'neutral'

    def act(self):
        action = HodorAction(self.mood)
        return action.get()


class HodorAction(object):

    def __init__(self, mood):
        self.possibleactions = []
        self.mood = mood
        self.total_weight = 0
        self.load()

    def add(self, action):
        self.total_weight += action['weight']
        self.possibleactions.append(action)

    def get(self):
        if self.total_weight is 0:
            return False
        winning_number = random.randint(0, self.total_weight)
        running_total = 0
        for cur_action in self.possibleactions:
            running_total += cur_action['weight']
            if running_total >= winning_number:
                return cur_action['action']

    def load(self):
        for mood, action_list in HodorActions.actions.iteritems():
            if mood is self.mood:
                for cur_action in action_list:
                    self.add(cur_action)
