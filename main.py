import logging

import event_manager
import controller
import game
import events

logger = logging.getLogger(__name__)

ev = event_manager.EventManager()
c = controller.Controller(ev)
g = game.Game(ev)
ev.post(events.TickEvent())
g.startgame()
ev.post(events.TickEvent())

def main():
    c.run()

if __name__ == '__main__':
    main()
