from Options import DeathLink, PerGameCommonOptions, Choice


class EndGoal(Choice):
    """The end goal required to beat the game.
    Vanilla: Finish the vanilla storyline.

    Dark Side: Beat Dark Side

    Darker Side: Beat Darker Side
    """
    display_name = "End Goal"
    option_vanilla = 1
    option_dark = 2
    option_darker = 3
    default = 1

class KingdomRandomizer(Choice):
    """Shuffles the order that kingdoms get unlocked.
    Light means that kingdoms get shuffled but Moon, Dark and Darker still appear last.
    Insanity means there is no such rules."""

    display_name = "Shuffle Kingdoms"
    option_false=0
    option_light = 1
    option_insanity = 2
    default = 1

class RandomizeCosmetics(Choice):
    """Puts Mario's Outfits into the itempool"""
    display_name = "Randomize Cosmetics"
    option_false = 0
    option_true = 1
    default = 0

class RandomizeMovement(Choice):
    """Puts Mario's Movement Abilities into the itempool"""
    display_name = "Randomize Movement"
    option_false = 0
    option_true = 1
    default = 0

class SMOOptions(PerGameCommonOptions):
    EndGoal: EndGoal
    KingdomRandomizer:  KingdomRandomizer
    RandomizeCosmetics: RandomizeCosmetics
    RandomizeMovement:  RandomizeMovement
    death_link:         DeathLink