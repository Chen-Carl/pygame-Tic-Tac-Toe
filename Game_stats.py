class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.game_active = False
        self.piece_choose = 0
        self.add_new_piece = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.boxes_status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
