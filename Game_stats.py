class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.game_active = True
        self.add_new_piece = False
        self.mouse_x = 0
        self.mouse_y = 0