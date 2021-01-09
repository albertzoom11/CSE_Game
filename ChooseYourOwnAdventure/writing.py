'''
Project Name: Choose Your Own Adventure
Team Members: Albert Zou, Benjamin Knobloch, Kyle DiMaggio
Date: February 13
Task Description: Contains the game's written dialogue.
'''

class Writing:
    playerName = ""
    pronoun = "she"

    def __init__(self, playerName, gender):
        self.playerName = playerName
        if gender == "male":
            self.pronoun = "he"       

    def chanas1(self):
        return ["Why aren't you in class!?",
                    "You were in the bathroom?",
                    "Fair enough. But you shouldn't be here.",
                    "This isn't a drill. This is the real thing.",
                    "I can't let you in the room, so you should leave the school.",
                    "Take the stairs. Go left, and the unlocked door is an exit.",
                    "Use the WASD keys to move, and click on objects and doors to interact with them.",
                    "Good luck!"]
    
    def chanas2(self):
        return["You should hurry up and leave before something happens.",
                    "The stairwell is on the left. Get going!"]
    
    def chanas3(self):
        return ["What? Brian chased you inside?",
                    "Looks like there's no getting out of here then.",
                    "At least, not on foot...",
                    "I should probably explain what's going on.",
                    "Brian has been planning to destroy High Tech.",
                    "A few of the teachers know, and we're working together to stop him.",
                    "If Brian's outside, it's probably safe to let you in my room.",
                    "Unless... You want to help us?",
                    "Here, you'll need a few things.",
                    "You can see what's inside your backpack by pressing 'E'.",
                    "It's not magic, though! The more items you pick up, the slower you'll be.",
                    "I've also given you a flashlight so you can enter dark rooms. Unfortunately, I don't have any batteries.",
                    "I had one before, but I must have dropped it in the bushes as I was running through the courtyard.",
                    "You're our only hope if we're to save High Tech from the menace of Brian!",
                    "Good luck!"]

    def babbin1(self):
        return ["It's about time that you showed up!",
                "Brian isn't waiting around for us to save the school, you know.",
                "Anyway, let's cut to the chase.",
                "You may know me as \"Mrs. Babbin\", but I'm actually the Potion Master of High Tech.",
                "With the right ingredients, I can make any potion which could help us get us out of this jam.",
                "Unfortunately, Brian raided my whole stock when the power went out.",
                "Even now, Brian could be preparing a potion with enough power to obliterate High Tech.",
                "We can't let that happen!",
                "I'll need your help to get the ingredients you need to proceed.",
                "If you have an ingredient which you think I can turn into a potion, just use the item on me."]

    def babbin2(self):
        return ["THINKINGHmmm...",
                "THINKINGA substance containing a lot of sugar could be turned into a pretty good fuel..."]
    def babbin3(self):
        return ["THINKINGHmmm...",
                "THINKINGI may be able to amplify the metabolic power of a substance containing a lot of protein..."]
    def babbin4(self):
        return ["Take this fuel!"]

    def adithya1(self):
        return [""]
    
    def brian1(self):
        return [""]
    
    def joe1(self):
        return [""]
    
    def alber1(self):
        return [""]

    def ben1(self):
        return [""]
    
    def mullarkey(self):
        return["Huh?",
                "How did you get in here?",
                "Nevermind. We have more important things to worry about.",
                "I've got two objects here that might be useful to you.",
                "The first is the key to the Darby Cart.",
                "If you want to escape, this may be what you want.",
                "I also have an Nspire.",
                "Brian can sense the presence of mathematical devices.",
                "If you were to place this calculator on an object of thaumaturgical significance, you may be able to summon Brian to your location.",
                "That could be very dangerous if you don't know what you're doing.",
                "Also keep in mind that every item you hold slows you down.",
                "You may not want to take both of these.",
                "Choose wisely."]

    def stephen(self):
        return ["When you leave the room and I despawn, what will happen to me?",
        "I hope it doesn't hurt."]
    def stephen1(self):
        return ["Have you wondered why we all look like collections of solidly-colored blocks?",
        "I've thought about it a bit."]
    def stephen2(self):
        return ["Sorry, bud. I don't have any side quests for you."]
    def stephen3(self):
        return ["Why are all the lockers closed?",
        "I bet the developers of this game were too lazy to make unique art for each one."]
    def stephen4(self):
        return ["Did you know that we live in a simulation?"]
    
    def brendan1(self):
        return ["Oh...",
        "Oh man...",
        "This isn't going very well.",
        "Hey, you!",
        "Do you have a battery I can borrow?",
        "THINKING...",
        "What do you mean it's a lockdown?",
        "I've got to finish my circuit!",
        "THINKINGOh God. I really wish I didn't eat my only battery."]

    def brendan2(self):
        return ["Oh! A battery!",
        "This is just what I needed!",
        "How did you know?",
        "Oh, right. I told you.",
        "Well let's just pop this baby right in, shall we?",
        "THINKING...",
        "Uh... which way does it go in again?",
        "Nevermind, nevermind. I've got it.",
        "THINKING...",
        "COMMANDSHOOT!!!",
        "I put it in the wrong way!",
        "Uh oh.",
        "Quick! Put out the fire!",
        "If only I could remember which fire extinguisher to use...",]

    def god1(self):
        return ["Moses! Moses!",
            "Oh, sorry. I thought you were someone else.",
            "I've been in a bit of a rush, you see.",
            "Is there any adult there I can speak to?",
            "Are you sure? It's quite important.",
            "No one? No one at all?",
            "Great. Just great!",
            "THINKINGThis is bad, this is bad...",
            "THINKINGWhat do I do?",
            "THINKINGI'd say \"God knows,\" but I don't.",
            "THINKINGWell, what about this one here?",
            "THINKING" + self.pronoun[0].upper() + self.pronoun[1:] + "'s a bit sickly looking, if I'm being honest...",
            "THINKINGHmmm... Well, "  + self.pronoun + "'ll have to do, I suppose.",
            "THINKING*Ahem*",
            "Step forth, mortal!",
            "Tremble before me!",
            "I am God Almighty, Creator of Heaven and Earth!",
            "Sorry for the appearance. I hope this bush wasn't important to you.",
            "I am calling upon you, " + self.playerName + ", because...",
            "THINKING...",
            "Okay, you can stop trembling now. It's getting a little distracting.",
            "THINKING...",
            "Anyway...",
            "THINKING*Ahem*",
            "I am calling upon you, " + self.playerName + ", because I have seen signs that something is terribly wrong where you are.",
            "A great evil has taken residence in this very high school.",
            "It is none other than a terrible demon, escaped from Hell and wrought on bringing misery to mankind.",
            "This demon has possessed a human, whom it plans to use to carry out its malicious deeds of unspeakable horror.",
            "Only you can find a way to stop this demon and bring salvation to High Technology High School.",
            "Now go, " + self.playerName + ", and do what you must!",
            "THINKING...",
            "Well, what are you waiting for?",
            "What do you mean you want me to explain how to play the game to you?",
            "What am I, a bloody instruction manual? Jesus Christ!",
            "That's my son, by the way.",
            "Oh, alright, alright. Here it goes.",
            "Let's see here...",
            "\"Use the WASD keys to mo...\" How old do they think you are, four? Let's skip ahead a little.",
            "\"Click on items of interest to interact with them or pick them up.\"",
            "\"Items you pick up will be put into your inventory (your backpack).\"",
            "\"Press \'e\' to open your inventory.\"",
            "\"Click on items in your inventory to put them in your hand.\"",
            "\"When in your hand, items can be used on other items or on objects in the world.\"",
            "\"However, remember that your inventory space is limited.\"",
            "\"It's dark in the school, so perhaps your first goal should be to find a flashlight.\"",
            "\"You'll probably need batteries to operate it. Two should do the trick.\"",
            "Okay, that's enough of that.",
            "If you need any help, come speak to me.",
            "I'm not going anywhere, believe me. You know, omnipresence and all that junk.",
            "THINKINGUgh ... stuck here with this nitwit in a dirty bush ... I hope this game isn't long.",
            "Well? What are you waiting for? Go!"]

    def god2(self):
        return ["What? You're already stuck?",
            "THINKINGWe could be in worse trouble than I thought.",
            "Were you listening the first time I read the instructions?",
            "I bet not.",
            "You're lucky I have nowhere else to be right now, or you might have to *gasp* figure something out on your own.",
            "\"Click on items of interest to interact with them or pick them up.\"",
            "\"However, remember that your inventory space is limited.\"",
            "\"It's dark in the school, so perhaps your first goal should be to find a flashlight.\"",
            "\"You'll probably need batteries to operate it. Two should do the trick.\"",
            "Got all that?",
            "THINKINGHumans... sheesh."]

    def easterEggGod(self):
        return ["Moses! Moses!",
        "Oh, sorry. I thought you were someone else.",
        "THINKINGAhem...",
        "Step forth, mortal!",
        "Tremble before me!",
        "I am God Almighty, Creator of Heaven and Earth!",
        "Sorry for th...",
        "THINKING...",
        "Okay, you can stop trembling now. It's getting a little distracting.",
        "THINKING...",
        "THINKINGAhem...",
        "Sorry for the appearance. I hope this bush wasn't important to you.",
        "I have descended from my heavenly loft to speak to you of a matter of divine importance.",
        "It is my solemn duty to bestow upon you a quest.",
        "This quest may very well decide the fate of humanity.",
        "So, what do you say?",
        "Will you accept this holy mission and complete the true mission of God?",
        "THINKING...",
        "THINKING...",
        "THINKING...",
        "Hello?",
        "Are you going to respond?",
        "THINKING...",
        "Did you call me down into a dirty bush just to sit and stare at me like an imbecile?",
        "Jesus Christ! Why do I even try?",
        "I could solve your entire problem, ya know.",
        "Omnipotence and all that junk. It's real.",
        "Yep, I could snap my fingers and you could win this game right this second.",
        "But I'm NOT GONNA DO IT.",
        "See how it feels?",
        "I bet you do."]

    def phantombunny(self):
        return ["OUR FATHER",
        "WHO ART IN HEAVEN",
        "HALLOWED BE THY NAME",
        "THY KINGDOM COME",
        "THY WILL BE DONE",
        "ON EARTH AS IT IS IN HEAVEN.",
        "GIVE US THIS DAY",
        "OUR DAILY BREAD",
        "AND FORGIVE US OUR TRESPASSES",
        "AS WE FORGIVE THOSE",
        "WHO TRESPASS AGAINST US",
        "AND LEAD US NOT",
        "INTO TEMPTATION",
        "BUT DELIVER US FROM EVIL",
        "AMEN."]