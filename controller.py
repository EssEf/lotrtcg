import events

class Controller:
    def __init__(self, ev):
        self.ev = ev

    def run(self):
        while True:
            self.ev.post(events.TickEvent())
