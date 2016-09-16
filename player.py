import notifiable
import cards.card as card
import deck
import uid


class Player(notifiable.Notifiable, uid.UID):
    def __init__(self, ev, game, uid=None):
        super(Player, self).__init__(uid)

        self.ev = ev
        ev.registerListener(self)

        self.game = game

        self.hand = deck.Deck(visible=True)

        self.deck = deck.Deck(
            cards=[
                card.Companion(),
                card.Companion(),
                card.Companion(),
                card.Companion(),
                card.Companion(),
                card.Companion(),
                card.Minion(),
                card.Minion(),
                card.Minion(),
                card.Minion(),
                card.Minion(),
                card.Minion(),
                card.Minion(),
            ],
        )

        self.play_area = deck.Deck(visible=True)
        self.active = False
        self.discard = deck.Deck()
        self.name = 'Hallo'

    def handle_DrawCardEvent(self, e):
        if e.player_id == self.uid:
            self.hand.add(self.deck.draw())

    def __repr__(self):
        return '\n'.join([
            "Player: " + self.name,
            repr(self.discard) + " " + repr(self.deck) + " " + repr(self.play_area),
            repr(self.hand),
        ])

    def get_playable(self):
        return [c for c in self.hand if c.is_playable(self.game, self)]

    def play_card(self, card_id):
        for card in self.hand:
            if card.uid == card_id:
                self.hand.remove(card)
                self.play_area.add(card)
