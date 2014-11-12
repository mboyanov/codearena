__author__ = 'mboyanov'

class Unit:

    def __init__(self,data):
        self.id=data['id']
        self.x=data['x']
        self.y=data['y']
        self.orientation=data['orientation']
        self.level=data['level']
        self.player=data['player']
        if 'sees' in data:
            self.sees=data['sees']