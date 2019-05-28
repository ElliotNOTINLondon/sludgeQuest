from fighter import Fighter
from ai import *
from entity import Entity
from render_functions import RenderOrder


'''
COMMON ENEMIES 
'''


# PLANTS
def whip_vine(x, y):
    fighter_component = Fighter(current_hp=4, max_hp=4, damage_dice=1, damage_sides=2, armour=1,
                                strength=14, dexterity=6, vitality=10, intellect=0, perception=0, xp=25,
                                dodges=False)
    ai_component = Stationary()
    return Entity(x, y, 'V', libtcod.light_grey, 'Whip Vine',
                  'What at first appears to be no more than a dead, waist-height bush in actuality '
                  'represents a highly specialized carnivorous plant that flays the skin off any creature '
                  'that wanders into its path.',
                  blocks=True, render_order=RenderOrder.PLANT, fighter=fighter_component, ai=ai_component,
                  faction='Plants')


def phosphorescent_dahlia(x, y):
    fighter_component = Fighter(current_hp=1, max_hp=1, damage_dice=0, damage_sides=0, armour=0,
                                strength=0, dexterity=0, vitality=10, intellect=0, perception=16, xp=0,
                                dodges=False)
    ai_component = PassiveStationary()
    return Entity(x, y, 'd', libtcod.light_azure, 'Phosphorescent Dahlia',
                  'A common but perplexing sight within the SludgeWorks is to observe a brilliant flash of blue light, '
                  'instantaneously illuminating an entire cave section like a flash of lightning. The phosphorescent '
                  'dahlia is a well-known source of such flashes in this spectral region; a delicate plant which has '
                  'developed what some consider a visually offensive method of attracting pollinators.',
                  blocks=False, render_order=RenderOrder.PLANT, fighter=fighter_component, ai=ai_component,
                  regenerates=False, faction='Plants')


# SCAVENGERS
def wretch(x, y):
    fighter_component = Fighter(current_hp=4, max_hp=4, damage_dice=1, damage_sides=3, armour=0,
                                strength=14, dexterity=10, vitality=12, intellect=8, perception=10, xp=30,
                                dodges=True)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'w', libtcod.darker_red, 'Wretch',
                  'A stunted human swaddled in filthy rags and long since driven feral by the SludgeWorks.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Scavengers', erraticity=25)


def sludge_fiend(x, y):
    fighter_component = Fighter(current_hp=6, max_hp=6, damage_dice=1, damage_sides=5, armour=0,
                                strength=16, dexterity=8, vitality=10, intellect=6, perception=8, xp=50,
                                dodges=True)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'f', libtcod.red, 'Sludge Fiend',
                  'The irony of attempting to retain one\'s humanity whilst simultaneously seeking to consume '
                  'all mutagenic material in one\'s path seems to be lost on this poor unfortunate. Tattered clothing '
                  'drips off this mutant\'s twisted form like a bullet-shredded cape; obsidian spikes protrude '
                  'in clusters from its emaciated and discoloured torso.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Scavengers', erraticity=50)


def thresher(x, y):
        fighter_component = Fighter(current_hp=26, max_hp=26, damage_dice=2, damage_sides=6, armour=3,
                                    strength=20, dexterity=12, vitality=12, intellect=5, perception=8, xp=275,
                                    dodges=True)
        ai_component = AimlessWanderer()
        return Entity(x, y, 'T', libtcod.dark_azure, 'Thresher',
                      'A colossal ogre-like hominid covered in patches of matted hair and littered with scars. This '
                      'creature tirelessly searches it\'s surroundings for new objects to smash together with a '
                      'joyous, childlike expression.',
                      blocks=True, fighter=fighter_component, render_order=RenderOrder.ACTOR, ai=ai_component,
                      regenerates=True, faction='Scavengers', erraticity=75)


# BEASTS
def moire_beast(x, y):
    fighter_component = Fighter(current_hp=14, max_hp=14, damage_dice=3, damage_sides=2, armour=1,
                                strength=12, dexterity=16, vitality=12, intellect=10, perception=10, xp=200,
                                dodges=True)
    ai_component = Aggressive()
    return Entity(x, y, 'M', libtcod.light_grey, 'Moire Beast',
                  'The hide of this squat quadruped is an affront to the senses; dense and intricate greyscale '
                  'patterns constantly shift epileptically upon the beast\'s surface like a surrealist '
                  'interpretation of a zebra. The gleam of it\'s fluorescent yellow, feline irises serve as the only '
                  'ubiquitous reference point on this beast\'s wildly fluctuating, migraine-inducing form.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Beasts')


def lupine_terror(x, y):
    fighter_component = Fighter(current_hp=19, max_hp=19, damage_dice=5, damage_sides=2, armour=1,
                                strength=16, dexterity=14, vitality=10, intellect=6, perception=14, xp=200,
                                dodges=True)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'L', libtcod.light_grey, 'Lupine Terror',
                  'Evolutionary forces have twisted what must undeniably once have been a feral wolf into a horrific '
                  'vision of fangs and matted, grey fur. This monstrosity walks upright in emulation of nature\'s most '
                  'infamous apex predators as blood-tinged saliva hangs from it\'s constantly masticating jaws.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Beasts', erraticity=50)


def bloodseeker(x, y):
    fighter_component = Fighter(current_hp=82, max_hp=82, damage_dice=6, damage_sides=8, armour=10,
                                strength=30, dexterity=20, vitality=18, intellect=14, perception=14, xp=1000,
                                dodges=False)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'B', libtcod.light_crimson, 'Bloodseeker',
                  'An asymmetric monstrosity the size of a bear with a grinning, skinless snout. Rusted weaponry from '
                  'previous encounters juts from it\'s hide like gruesome jewellery, with pale, twisted flesh creeping '
                  'up the hilts. The creature\'s eyes are consumed by feral rage as it prowls the caverns, twitching '
                  'from the eternal	state of pain inflicted by its inherent regeneration.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Beast', erraticity=100)


# CULTISTS
def risen_sacrifice(x, y):
    fighter_component = Fighter(current_hp=randint(3, 7), max_hp=20, damage_dice=1, damage_sides=4, armour=0,
                                strength=12, dexterity=12, vitality=10, intellect=10, perception=10, xp=40,
                                dodges=True)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'r', libtcod.lightest_fuchsia, 'Risen Sacrifice',
                  'For those who have never encountered them, it is very easy to dismiss the Cult of Eternity as '
                  'a sect of aimless madmen with an obsessive focus upon human sacrifice. Those who have seen the '
                  'radiant bodies of the recently sacrificed reanimating joyfully, with blood still flowing from their '
                  'mortal wounds would strongly disagree with this statement.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  faction='Cultists', erraticity=34)


def eternal_celebrant(x, y):
    fighter_component = Fighter(current_hp=8, max_hp=8, damage_dice=2, damage_sides=2, armour=1,
                                strength=8, dexterity=12, vitality=18, intellect=16, perception=10, xp=160,
                                dodges=True)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'c', libtcod.light_purple, 'Eternal Cult Celebrant',
                  'The celebrant\'s dour, puckered form desperately hauls itself through the scratch-marked tunnels '
                  'towards the blissful murmurs of his newly-risen flock. \"Sweet children, where are you?\" he cries '
                  'out; a worn, sacrificial dagger trembles within his hand, piercing the suffocating darkness in '
                  'search of replies.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  faction='Cultists', erraticity=100)


def eternal_kidnapper(x, y):
    fighter_component = Fighter(current_hp=10, max_hp=10, damage_dice=2, damage_sides=4, armour=2,
                                strength=18, dexterity=10, vitality=12, intellect=10, perception=18, xp=200,
                                dodges=True)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'k', libtcod.light_fuchsia, 'Eternal Cult Kidnapper',
                  'By far the most notorious member of the Cult of Eternity and arguably serving the most '
                  'necessary role within their hierarchy. Their mission is simple: Kidnap the most virginal '
                  'entrants into the SludgeWorks so that the flow of flesh into the Palace of Hedonism is '
                  'constant and plentiful. The way they creep through the caverns with their threatening iron '
                  'blackjack makes this intention undeniably clear.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Cultists', erraticity=67)


# CLEANSING HAND
def cleansing_hand_crusader(x, y):
    fighter_component = Fighter(current_hp=22, max_hp=22, damage_dice=3, damage_sides=4, armour=4,
                                strength=22, dexterity=16, vitality=14, intellect=12, perception=12, xp=350,
                                dodges=True)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'C', libtcod.yellow, 'Cleansing Hand Crusader',
                  'The staple foot soldier of the Cleansing Hand. With his bucket helm, emblazoned tabard and well-'
                  'maintained platemail it is easy to see how these defenders of the faith are commonly known as '
                  'crusaders. Their tactics, however, as anything but medieval - intimidatingly rigorous discipline '
                  'combined with years of experience slaying deformed monstrosities leaves the crusaders fully able '
                  'to hold their own against many daily challenges experienced within the SludgeWorks.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Cleansing Hand', erraticity=67)


def cleansing_hand_purifier(x, y):
    fighter_component = Fighter(current_hp=32, max_hp=32, damage_dice=2, damage_sides=6, armour=4,
                                strength=24, dexterity=14, vitality=16, intellect=10, perception=14, xp=425,
                                dodges=True)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'P', libtcod.dark_yellow, 'Cleansing Hand Purifier',
                  'The purifier breathes deeply and calmly as his mail-clad fists tighten around the hilt of his '
                  'terrifying, studded morningstar. Although you cannot see any human flesh underneath his plated and '
                  'visored form you can be assured that what lies within is utterly untouched by the corrupting '
                  'influence of the SludgeWorks, and utterly devoted to preventing further horrific incursions into '
                  'Cleansing Hand territory. Never again will the last bastion of purity be defiled by such entropy.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Cleansing Hand', erraticity=14)


# HORRORS
def hunchback(x, y):
    fighter_component = Fighter(current_hp=12, max_hp=12, damage_dice=1, damage_sides=8, armour=1,
                                strength=18, dexterity=6, vitality=8, intellect=12, perception=10, xp=150,
                                dodges=True)
    ai_component = Aggressive()
    return Entity(x, y, 'H', libtcod.brass, 'Hunchback',
                  'A stunted and broken humanoid draped in tattered linen stained with the characteristic ochre '
                  'of dried blood. It\'s face is completely concealed by a tapered hood; the glint of a wicked '
                  'kirpan scatters all nearby light. Echoes of guttural chanting reverberate off the cave '
                  'walls as it glacially stumbles forward towards its next target.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Horrors', erraticity=10)


'''
UNIQUE ENEMIES
'''


# CLEANSING HAND
def alfonrice(x, y):
    fighter_component = Fighter(current_hp=42, max_hp=42, damage_dice=8, damage_sides=4, armour=6,
                                strength=28, dexterity=28, vitality=18, intellect=16, perception=18, xp=1550)
    ai_component = AimlessWanderer()
    return Entity(x, y, 'A', libtcod.light_yellow, 'Alfonrice, the Spinning Blade',
                  'The Cleansing Hand\'s most pious duelist Alfonrice earned his moniker not from the constant'
                  'twirling of his offhand swordbreaker, but from his proficiency in dispatching hordes of filthy '
                  'horrors with a single cleave of his cruciform broadsword. He grits his teeth in anticipation, '
                  'anxious to cut down the next prospective entrant to the Most Holy Bastion.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Cleansing Hand', erraticity=50)


def teague(x, y):
    fighter_component = Fighter(current_hp=64, max_hp=64, damage_dice=4, damage_sides=4, armour=0,
                                strength=20, dexterity=20, vitality=20, intellect=20, perception=20, xp=2500)
    ai_component = Aggressive()
    return Entity(x, y, 'T', libtcod.darkest_yellow, 'Teague the Martyr',
                  'The remnants of a dust-drenched, threadbare robe cling desperately to Teague\'s gaunt form '
                  'as he turns his gaze towards you. Despite decades of imprisonment, his skin is unblemished and pure '
                  'like that of a newborn child, and he calmly stares you down with unabashed superiority. One could '
                  'say that his entire life has been building up to this moment, and you are all that stands in the '
                  'way between him and complete control of the Bastion. The crusader\'s greatest shame and most '
                  'defiled heiromonk bows elegantly, politely inviting you to be cleansed by his own hands.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Cleansing Hand')


# CULTISTS
def dymacia(x, y):
    fighter_component = Fighter(current_hp=48, max_hp=48, damage_dice=1, damage_sides=6, armour=2,
                                strength=20, dexterity=20, vitality=24, intellect=30, perception=26, xp=2000)
    ai_component = Aggressive()
    return Entity(x, y, 'D', libtcod.darkest_fuchsia, 'Dymacia, Effigy of Perfection',
                  'Lovingly adorned with countless rosaries, letters of worship and symbolic mirrors, Dymanikos '
                  'effortlessly demonstrates her ability to command unfaltering loyalty in her followers. At least '
                  'eight feet tall, her towering stature is coupled with an inhumanly soothing voice that fills the '
                  'cathedral with pure, monotone chant. This woman appears to be wholly unarmed, but you are not so '
                  'easily deceived to think this she has ascended to a position of such power due to her weaknesses.',
                  blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component,
                  regenerates=True, faction='Cultists')
