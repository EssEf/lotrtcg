import uid

class Card(uid.UID):
    def __init__(self, uid=None):
        super(Card, self).__init__(uid)

    def __repr__(self):
        return self.name

    def is_playable(self, game, player):
        return True


class FreePeoples(Card):
    def is_playable(self, game, player):
        return (
            super(FreePeoples, self).is_playable(game, player)
            and player == game.get_free_peoples_player()
        )


class Companion(FreePeoples):
    def __init__(self, uid=None):
        super(Companion, self).__init__(uid)

        self.cost = 3
        self.max_hp = 4
        self.hp = 4
        self.strength = 3
        self.name = 'C'

    def is_playable(self, game, player):
        return (
            super(Companion, self).is_playable(game, player)
            and game.pm.get_phase() == 'fellowship'
        )


class Shadow(Card):
    def is_playable(self, game, player):
        return (
            super(Shadow, self).is_playable(game, player)
            and player in game.get_shadow_players()
        )


class Minion(Shadow):
    def __init__(self, uid=None):
        super(Minion, self).__init__(uid)

        self.cost = 4
        self.max_hp = 2
        self.hp = 2
        self.strength = 4
        self.name = 'M'

    def is_playable(self, game, player):
        return (
            super(Minion, self).is_playable(game, player)
            and game.pm.get_phase() == 'shadow'
            and game.twilight_pool >= self.cost
        )
