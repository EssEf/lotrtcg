import notifiable
import events


class PhaseManager(notifiable.Notifiable):
    def __init__(self, ev, game):
        self.ev = ev
        self.game = game
        ev.registerListener(self)
        self.phases = [
            'fellowship',
            'shadow',
        ]
        self.phase = -1

    def next_phase(self):
        self.phase += 1
        if self.phase > len(self.phases):
            self.phase = 0
        handle = 'enter_' + self.get_phase()
        if hasattr(self, handle) and hasattr(getattr(self, handle), '__call__'):
            getattr(self, handle)()

    def handle_NextPhaseEvent(self, e):
        self.next_phase() 

    def enter_shadow(self):
        self.ev.post(events.AllowPlayCardEvent(self.game.get_shadow_players[0]))

    def get_phase(self):
        return self.phases[self.phase]
