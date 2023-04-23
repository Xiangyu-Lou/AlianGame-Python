class GameStatus:
    """ track the game status """
    def __init__(self,ai_game):
        self.setting = ai_game.settings
        self.resert_status()
        
    def reset_status(self):
        """ reset the game information """