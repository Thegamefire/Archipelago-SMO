from worlds.AutoWorld import World
from .Options import SMOOptions


class SuperMarioOdysseyWorld(World):

    game = "Super Mario Odyssey"
    options_dataclass = SMOOptions
    options: SMOOptions


    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

