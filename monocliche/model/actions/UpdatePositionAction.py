from monocliche.model import Game
from monocliche.model.AbstractAction import AbstractAction


class UpdatePositionAction(AbstractAction):
    """
    This class represents an action in which it is necessary to change the position
    of a player for certain number of squares forward or backward.
    """

    def __init__(self, position_to_change: int):
        self.__position_to_change = position_to_change

    def execute(self, game: Game):
        # FIXME: need to use the service to update the player's position !?
        game.players.current_player.position += self.__position_to_change
