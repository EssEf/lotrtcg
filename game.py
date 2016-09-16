import notifiable
import player
import phase_manager
import events


class Game(notifiable.Notifiable):
    def __init__(self, ev):
        self.ev = ev
        ev.registerListener(self)

        self.pm = phase_manager.PhaseManager(ev, self)

        self.players = [
            player.Player(ev, self),
            player.Player(ev, self),
        ]
        self.fp_player = self.players[0]
        self.non_fp_players = self.players[1:]
        self.twilight_pool = 10

    def __repr__(self):
        return '\n'.join(repr(p) for p in self.players)

    def startgame(self):
        for _ in range(8):
            self.ev.post(events.DrawCardEvent(self.players[0].uid))
            self.ev.post(events.DrawCardEvent(self.players[1].uid))
        self.ev.post(events.NextPhaseEvent())

    def get_free_peoples_player(self):
        return self.fp_player

    def get_shadow_players(self):
        return self.non_fp_players

    def handle_PlayCardEvent(self, e):
        for player in players:
            if player.uid == e.player_id:
                player.play_card(e.card_id)
