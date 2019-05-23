from fighter import Fighter
from ai import *
from entity import Entity
from render_functions import RenderOrder

'''
COMMON ENEMIES 
'''


# PLANTS
def whip_vine(x, y):
    # Whip Vine
    fighter_component = Fighter(current_hp=8, max_hp=8, damage_dice=1, damage_sides=2,
                                strength=3, agility=1, vitality=1, intellect=1, perception=1, xp=25)
    ai_component = Stationary()
    return Entity(x, y, 'V', libtcod.light_grey, 'Whip Vine',
                  'What at first appears to be no more than a dead, waist-height bush in actuality '
                  'represents a highly specialized carnivorous plant that flays the skin off any creature '
                  'that wanders into its path.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  faction='Plants')


# SCAVENGERS
def wretch(x, y):
    fighter_component = Fighter(current_hp=4, max_hp=4, damage_dice=1, damage_sides=3,
                                strength=2, agility=1, vitality=1, intellect=1, perception=1, xp=30)
    ai_component = Aggressive()
    return Entity(x, y, 'w', libtcod.darker_red, 'Wretch',
                  'A stunted human swaddled in filthy rags and long since driven feral by the SludgeWorks.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  faction='Scavengers')


def sludge_fiend(x, y):
    fighter_component = Fighter(current_hp=9, max_hp=9, damage_dice=3, damage_sides=2,
                                strength=2, agility=2, vitality=1, intellect=1, perception=1, xp=50)
    ai_component = Aggressive()
    return Entity(x, y, 'f', libtcod.dark_red, 'Sludge Fiend',
                  'The irony of attempting to retain one\'s humanity whilst simultaneously seeking to consume '
                  'all mutagenic material in one\'s path seems to be lost on this creature. Tattered clothing '
                  'flows off this mutant\'s twisted form like a bullet-shredded cape, with obsidian spikes protruding '
                  'in clusters from its gaunt, discoloured body.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  faction='Scavengers')


def thresher(x, y):
        fighter_component = Fighter(current_hp=26, max_hp=26, damage_dice=3, damage_sides=5,
                                    strength=5, agility=4, vitality=1, intellect=1, perception=1, xp=225)
        ai_component = Aggressive()
        return Entity(x, y, 'T', libtcod.dark_azure, 'Thresher',
                      'A colossal ogre-like hominid covered in patches of matted hair and littered with scars. This '
                      'creature tirelessly searches it\'s surroundings for new objects to smash together with a '
                      'joyous, childlike expression.',
                      blocks=True, fighter=fighter_component, render_order=RenderOrder.ACTOR, ai=ai_component,
                      faction='Scavengers')


def bloodseeker(x, y):
    fighter_component = Fighter(current_hp=56, max_hp=56, damage_dice=4, damage_sides=6,
                                strength=8, agility=4, vitality=1, intellect=1, perception=1, xp=500)
    ai_component = Aggressive()
    return Entity(x, y, 'B', libtcod.light_crimson, 'Bloodseeker',
                  'An asymmetric monstrosity the size of a bear with a grinning, skinless snout. Rusted weaponry from '
                  'previous encounters juts from it\'s hide like gruesome jewellery, with pale, twisted flesh creeping '
                  'up the hilts. The creature\'s eyes are consumed by feral rage as it prowls the caverns, twitching '
                  'from the eternal	state of pain inflicted by its inherent regeneration.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component,
                  ai=ai_component, faction='Scavengers')


# BEASTS
def moire_beast(x, y):
    fighter_component = Fighter(current_hp=14, max_hp=14, damage_dice=3, damage_sides=2,
                                strength=3, agility=7, vitality=1, intellect=1, perception=1, xp=200)
    ai_component = Aggressive()
    return Entity(x, y, 'M', libtcod.light_grey, 'Moire Beast',
                  'The hide of this squat quadruped is an affront to the senses; dense and intricate greyscale '
                  'patterns constantly shift epileptically upon the beast\'s surface like a surrealist '
                  'interpretation of a zebra. The gleam of it\'s fluorescent yellow, feline irises serve as the only '
                  'ubiquitous reference point on this beast\'s wildyly fluctuating, migraine-inducing form.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component,
                  ai=ai_component, faction='Beasts')


# CULTISTS
def risen_sacrifice(x, y):
    fighter_component = Fighter(current_hp=8, max_hp=8, damage_dice=2, damage_sides=2,
                                strength=2, agility=1, vitality=1, intellect=1, perception=1, xp=25)
    ai_component = Aggressive()
    return Entity(x, y, 'r', libtcod.lightest_fuchsia, 'Risen Sacrifice',
                  'For those who have never encountered them, it is very easy to dismiss the Cult of Eternity as '
                  'a sect of aimless madmen with an obsessive focus upon human sacrifice. Those who have seen the '
                  'radiant bodies of the recently sacrificed reanimating joyfully, with blood still flowing from their '
                  'mortal wounds would strongly disagree with this statement.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  faction='Cultists')


def eternal_kidnapper(x, y):
    fighter_component = Fighter(current_hp=14, max_hp=14, damage_dice=2, damage_sides=4,
                                strength=3, agility=6, vitality=1, intellect=1, perception=1, xp=100)
    ai_component = Aggressive()
    return Entity(x, y, 'k', libtcod.light_fuchsia, 'Eternal Kidnapper',
                  'By far the most notorious member of the Cult of Eternity and arguably serving the most '
                  'necessary role within their hierarchy. Their mission is simple: Kidnap the most virginal '
                  'entrants into the SludgeWorks so that the flow of flesh into the Palace of Hedonism is '
                  'constant and plentiful. The way they creep through the caverns with their threatening iron '
                  'blackjack makes this intention undeniably clear.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  faction='Cultists')


# CLEANSING HAND
def cleansing_hand_crusader(x, y):
    fighter_component = Fighter(current_hp=22, max_hp=22, damage_dice=3, damage_sides=4,
                                strength=4, agility=4, vitality=1, intellect=1, perception=1, xp=50)
    ai_component = Aggressive()
    return Entity(x, y, 'C', libtcod.yellow, 'Cleansing Hand Crusader',
                  'The staple foot soldier of the Cleansing Hand. With his bucket helm, emblazoned tabard and well-'
                  'maintained platemail it is easy to see how these defenders of the faith are commonly known as '
                  'crusaders. Their tactics, however, as anything but medieval - intimidatingly rigorous discipline '
                  'combined with years of experience slaying deformed monstrosities leaves the crusaders fully able '
                  'to hold their own against many daily challenges experienced within the SludgeWorks.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  faction='Cleansing Hand')


# HORRORS
def hunchback(x, y):
    fighter_component = Fighter(current_hp=12, max_hp=12, damage_dice=1, damage_sides=12,
                                strength=4, agility=0, vitality=1, intellect=1, perception=1, xp=125)
    ai_component = Aggressive()
    return Entity(x, y, 'H', libtcod.brass, 'Hunchback',
                  'A stunted and broken humanoid draped in tattered linen stained with the characteristic ochre '
                  'of dried blood. It\'s face is completely concealed by a tapered hood; the glint of a wicked '
                  'kirpan scatters all nearby light. Echoes of guttural chanting reverberate off the cave '
                  'walls as it glacially stumbles forward towards its next target.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component,
                  ai=ai_component, faction='Horrors')


'''
UNIQUE ENEMIES
'''


# CLEANSING HAND
def alfonrice(x, y):
    fighter_component = Fighter(current_hp=42, max_hp=42, damage_dice=4, damage_sides=4,
                                strength=6, agility=6, vitality=1, intellect=1, perception=1, xp=750)
    ai_component = Aggressive()
    return Entity(x, y, 'A', libtcod.light_yellow, 'Alfonrice, the Spinning Blade',
                  'The Cleansing Hand\'s most pious duelist Alfonrice earned his moniker not from the constant'
                  'twirling of his offhand swordbreaker, but from his proficiency in dispatching hordes of filthy'
                  'horrors with a single cleave of his cruciform broadsword. He grits his teeth in anticipation, '
                  'anxious to cut down the next prospective entrant to the Most Holy Bastion.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  faction='Cleansing Hand')
