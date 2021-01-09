'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Holds information about the game's sprites.
'''

import os

directory = os.path.dirname(os.path.abspath(__file__))  

# subtract 10 from line number for index of image
boyAvatars = [os.path.join(directory, 'assets/boyavatarfacingdown.png'),
    os.path.join(directory, 'assets/boyavatarfacingdownstepl.png'),
    os.path.join(directory, 'assets/boyavatarfacingdownstepr.png'),
    os.path.join(directory, 'assets/boyavatarfacingleft.png'),
    os.path.join(directory, 'assets/boyavatarfacingleftstepl.png'),
    os.path.join(directory, 'assets/boyavatarfacingleftstepr.png'),
    os.path.join(directory, 'assets/boyavatarfacingup.png'),
    os.path.join(directory, 'assets/boyavatarfacingupstepl.png'),
    os.path.join(directory, 'assets/boyavatarfacingupstepr.png'),
    os.path.join(directory, 'assets/boyavatarfacingright.png'),
    os.path.join(directory, 'assets/boyavatarfacingrightstepl.png'),
    os.path.join(directory, 'assets/boyavatarfacingrightstepr.png')]

girlAvatars = [os.path.join(directory, 'assets/girlavatarfacingdown.png'),
    os.path.join(directory, 'assets/girlavatarfacingdownstepl.png'),
    os.path.join(directory, 'assets/girlavatarfacingdownstepr.png'),
    os.path.join(directory, 'assets/girlavatarfacingleft.png'),
    os.path.join(directory, 'assets/girlavatarfacingleftstepl.png'),
    os.path.join(directory, 'assets/girlavatarfacingleftstepr.png'),
    os.path.join(directory, 'assets/girlavatarfacingup.png'),
    os.path.join(directory, 'assets/girlavatarfacingupstepl.png'),
    os.path.join(directory, 'assets/girlavatarfacingupstepr.png'),
    os.path.join(directory, 'assets/girlavatarfacingright.png'),
    os.path.join(directory, 'assets/girlavatarfacingrightstepl.png'),
    os.path.join(directory, 'assets/girlavatarfacingrightstepr.png')]

chanasAvatars = [os.path.join(directory, 'assets/mrhanasfacingdown.png'),
    os.path.join(directory, 'assets/mrhanasfacingleft.png'),
    os.path.join(directory, 'assets/mrhanasfacingup.png'),
    os.path.join(directory, 'assets/mrhanasfacingright.png')]

chanasSpyAvatars = [os.path.join(directory, 'assets/mrhanasspyfacingdown.png'),
    os.path.join(directory, 'assets/mrhanasspyfacingleft.png'),
    os.path.join(directory, 'assets/mrhanasspyfacingup.png'),
    os.path.join(directory, 'assets/mrhanasspyfacingright.png')]

babbinAvatars = [os.path.join(directory, 'assets/babbinfacingdown.png'),
    os.path.join(directory, 'assets/babbinfacingleft.png'),
    os.path.join(directory, 'assets/babbinfacingup.png'),
    os.path.join(directory, 'assets/babbinfacingright.png')]

mullarkeyAvatars = [os.path.join(directory, 'assets/mullarkeyfacingdown.png'),
    os.path.join(directory, 'assets/mullarkeyfacingleft.png'),
    os.path.join(directory, 'assets/mullarkeyfacingup.png'),
    os.path.join(directory, 'assets/mullarkeyfacingright.png')]

mrbAvatars = [os.path.join(directory, 'assets/mrbfacingdown.png'),
    os.path.join(directory, 'assets/mrbfacingleft.png'),
    os.path.join(directory, 'assets/mrbfacingup.png'),
    os.path.join(directory, 'assets/mrbfacingright.png')]

brendanAvatars = [os.path.join(directory, 'assets/brendanfacingdown.png'),
    os.path.join(directory, 'assets/brendanfacingleft.png'),
    os.path.join(directory, 'assets/brendanfacingup.png'),
    os.path.join(directory, 'assets/brendanfacingright.png')]

stephenAvatars = [os.path.join(directory, 'assets/stephenfacingdown.png'),
    os.path.join(directory, 'assets/stephenfacingleft.png'),
    os.path.join(directory, 'assets/stephenfacingup.png'),
    os.path.join(directory, 'assets/stephenfacingright.png')]

brianAvatars = [os.path.join(directory, 'assets/brianstanding.png'),
    os.path.join(directory, 'assets/brianfallen.png')]

uiBoxes = [os.path.join(directory, 'assets/dialoguebox.png'),
    os.path.join(directory, 'assets/infobox.png'),
    os.path.join(directory, 'assets/inventory.png')]

fish = os.path.join(directory, 'assets/redherring.png')

rooms = [os.path.join(directory, 'assets/nexus.png'),
    os.path.join(directory, 'assets/freshmanhallway.png'),
    os.path.join(directory, 'assets/freshmansophomorehallway.png'),
    os.path.join(directory, 'assets/sophomorejuniorhallway.png'),
    os.path.join(directory, 'assets/juniorhallway.png'),
    os.path.join(directory, 'assets/juniornexus.png'),
    os.path.join(directory, 'assets/boysbathroom.png'),
    os.path.join(directory, 'assets/courtyard.png'),
    os.path.join(directory, 'assets/mathroom.png'),
    os.path.join(directory, 'assets/chemroom.png'),
    os.path.join(directory, 'assets/stairwell.png'),
    os.path.join(directory, 'assets/cseroom.png'),
    os.path.join(directory, 'assets/outside.png'),
    os.path.join(directory, 'assets/darkroom.png')]

door = os.path.join(directory, 'assets/transparentdoor.png')

oldkey = os.path.join(directory, 'assets/oldfashionedkey.png')

bush = os.path.join(directory, 'assets/bush.png')

battery = os.path.join(directory, 'assets/battery.png')

hintdrawingitem = os.path.join(directory, 'assets/hintdrawingitem.png')

hintdrawing = os.path.join(directory, 'assets/hintdrawing.png')

god = os.path.join(directory, 'assets/god.png')

hanasface = os.path.join(directory, 'assets/hanasFace.jpg')

frosting = os.path.join(directory, 'assets/frosting.png')

balsface = os.path.join(directory, 'assets/balsFace.jpg')

loudspeaker = os.path.join(directory, 'assets/loudspeaker.jpg')

darbycart = os.path.join(directory, 'assets/darbycart.png')

icechunk = os.path.join(directory, 'assets/icechunk.png')

loudspeaker = os.path.join(directory, 'assets/loudspeaker.png')

fuel = os.path.join(directory, 'assets/gaspotion.png')

modernkey = os.path.join(directory, 'assets/modernkey.png')

icepick = os.path.join(directory, 'assets/icepick.png')

ice = os.path.join(directory, 'assets/ice.png')

titleCards = [os.path.join(directory, 'assets/titlecardvictorybyabandonment.png'),
            os.path.join(directory, 'assets/titlecardvictorybyabandonment1.png'),
            os.path.join(directory, 'assets/titlecardvictorybyabandonment2.png'),
            os.path.join(directory, 'assets/titlecardvictorybyice.png'),
            os.path.join(directory, 'assets/titlecardgameover.png'),
            os.path.join(directory, 'assets/titlecarddeathbypoison.png'),
            os.path.join(directory, 'assets/titlecarddeathbyfire.png')]

turkeysandwich = os.path.join(directory, 'assets/turkeysandwich.png')

exclamationmark = os.path.join(directory, 'assets/surpriseindicator.png')

speechbubble = os.path.join(directory, 'assets/speechindicator.png')

hamburger = os.path.join(directory, 'assets/hamburger.png')

fireextinguisher = [os.path.join(directory, 'assets/classafire.png'),
                    os.path.join(directory, 'assets/classbfire.png'),
                    os.path.join(directory, 'assets/classcfire.png'),
                    os.path.join(directory, 'assets/classdfire.png')]

circuit = os.path.join(directory, 'assets/circuit.png')

calculator = os.path.join(directory, 'assets/calculator.png')

flashlight = os.path.join(directory, 'assets/flashlightnotlit.png')

litflashlight = os.path.join(directory, 'assets/flashlightlit.png')

pedestal = os.path.join(directory, 'assets/pedestal.png')

mullarkeyface = os.path.join(directory, 'assets/mullarkey.jpg')

brianface = os.path.join(directory, 'assets/brianFace.jpg')

stephenface = os.path.join(directory, 'assets/stephenFace.jpg')

babbinface = os.path.join(directory, 'assets/babbinface.jpg')