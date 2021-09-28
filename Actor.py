   
class Actor:
    def __init__(self , a):
        self.actor = a

    def shows(self):
        actors = []
        actor = self.actor
        actor = actor.split(',')
        actors.append(actor)
        return actors