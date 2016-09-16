import logging
import weakref

import events

logger = logging.getLogger(__name__)


class EventManager:
    def __init__(self):
        self.listeners = weakref.WeakKeyDictionary()
        self.removed_listeners = []
        self.added_listeners = []
        self.event_queue = []

    def registerListener(self, listener):
        self.added_listeners.append(listener)

    def removeListener(self, listener):
        self.removed_listerners.append(listener)

    def post(self, e):
        if isinstance(e, events.TickEvent):
            self.consumeEvents()
        else:
            print('[EventManager]: Caught Event: %s' % e.__class__.__name__)
            self.event_queue.append(e)

    def consumeEvents(self):
        i = 0
        while i < len(self.event_queue):
            e = self.event_queue[i]
            for listener in self.listeners:
                listener.notify(e)
            i += 1
        self.event_queue = []
        while self.removed_listeners:
            listener = self.removed_listeners.pop()
            if listener in self.listeners:
                del self.listeners[listener]
        while self.added_listeners:
            listener = self.added_listeners.pop()
            self.listeners[listener] = 1
