from worlds.AutoWorld import World
from .Options import SMOOptions


class SuperMarioOdysseyWorld(World):

    game = "Super Mario Odyssey"
    options_dataclass = SMOOptions
    options: SMOOptions
