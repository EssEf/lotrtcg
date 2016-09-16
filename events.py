class Event:
    pass


class TickEvent(Event):
    pass


class DrawCardEvent(Event):
    def __init__(self, player_id):
        self.player_id = player_id


class NextPhaseEvent(Event):
    pass


class AllowPlayCardEvent(Event):
    def __init__(self, player_id):
        self.player_id = player_id


class PlayCardEvent(Event):
    def __init__(self, card_id, player_id):
        self.card_id = card_id
        self.player_id = player_id
