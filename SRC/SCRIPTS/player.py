#imports external
import pygame as pyg
#imports external
import SCRIPTS.utilities as _util
class PLAYER():
    def __init__(self, display: pyg.display, text_obj: _util.text_fonts):
        self.display = display
        self.util_obj = _util.utility(self.display)
        self.text_obj = text_obj
        self.player_info ={
            "day": 1,
            "casos_won": 0,
            "casos_lost": 0,
            "money": 100,
            "tutorial_done": False,
            "number_of_interrogations": 15,
            "vidas": 3
        }
        self.player_dialog = {
            "part": 0
        }
        self.dialog_already_seen = [
            {
                "ID": int,
                "NAME": str,
                "DIALOG": str
            }
        ]
        ...
    def dialog(self, list_dialog: list[str], continue_dialog: bool):
        block_pos = (self.display.get_width()/2, self.display.get_height()-10)
        block_size = (self.display.get_width(), 100)
        block_text = pyg.Surface(block_size).convert()
        block_text.fill("#ffffff")
        block_rect = block_text.get_rect(center=block_pos)
        self.display.blit(block_text, block_rect)
        self.text_obj.f_info["text"] = list_dialog[self.player_dialog["part"]]
        if continue_dialog and self.player_dialog["part"] != len(list_dialog):
            self.player_dialog["part"] += 1
            self.text_obj.f_animation["frame"] = 0
            return
        self.text_obj.long_text_dialog(10)
        self.text_obj.update()