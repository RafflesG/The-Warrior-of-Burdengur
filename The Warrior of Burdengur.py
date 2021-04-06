import time



print("\u001b[3mThe Warrior of Burdengur\u001b[0m")

print("\u001b[32mA: Start\u001b[0m")

print("\u001b[31mB: Quit \u001b[0m")

answer_1 = (input("Put button here "))

a_1 = ("A")
b_1 = ("B")
c_1 = ("C")

if answer_1 == a_1:
    print('If you see a "|" between different lines of text, it is just there to divide the text up.')
    name = (input("What are you going to name your warrior? "))
    print(f"{name} is a good name. He will be a fine warrior.")
    time.sleep(2)
    print(f"Once upon a time, in the kingdom of Burdengur, there was a child named {name}. He was born the son of the great warrior, Fyarl. Fyarl was one of the best warriors to ever grace the soil of Burdengur. He was born the son of the great cook, Miean. She was the lead cook at our kitchen at the castle. We knew that you would be perfect for an adventure. You could be trained by your father in the arts of combat, and learn how to cook in the ways of your mother. The queen and I kept an eye out for you, for a moment like this. Our Kingdom was just recently besieged by a dragon. We need your help to defeat this dragon, and to save the kingdom of Burdengur.")
    time.sleep(9)
    print(f'"{name}, come here." The king said. "You need to kill that dragon. He just ravaged through our kingdom. He destroyed tens of homes, killed 5 people, and left 23 wounded. He even destroyed the cabage mans cabages." I accepted the quest, knowing this would be the greatest challenge of my life.')
    print("|")
    time.sleep(4)
    print(f"Soon, the legends woul be told. The legend of the mighty warrior of burdengur. The one who slayed the dragon. The one who saved the kingdom. The one, they call {name}")
    print("|")
    print(f"{name} walks up to the mountain where the evil Dragon stands.")
    print("|")
    time.sleep(7)
    print("You see an enemy slime. What do you do? A. Fight the slime, B. Atempt to run")
    answer_2 = (input("Type answer here: "))
    if answer_2 == a_1:
        print("You slice at the slime. It gets sliced in half and disapates. You get some xp, and you levels up!")
        time.sleep(4)
        print("You walk higher and higher up the mountain, getting closer to the dragon's den. AS you get closer, you see a group of 2 slimes.")
        time.sleep(4)
        print("What do you do? A. Fight through the slimes, B. Run away")
        answer_3 = (input("Type answer here: "))
        if answer_3 == a_1:
            print("You slash at one of the slimes. It explodes, spurting slime all over you and the other slime. You walk towards the other slime, and trip and fall. As you fall, your sword slashes through the other slime, making it also explode.")
            print("You walk farther and farther up the mountain, until you reach a split in the road. A. Go left, B. Go right")
            answer_4 = (input("Put answer here: "))
            if answer_4 == a_1:
                print("You go left.")
                print("You walk up a steep slope, and walk into the lair of the dragon. He wakes up and screams out blazing fire. Your skin starts burning. The dragon looks at you. What do you do? A. Bring up your shield B. Roll away")
                answer_4_1 = (input("Put answer here: "))
                if answer_4_1 == a_1:
                    print("You bring up your shield. The dragon spits out fire at it, and it burns to a crisp. You run at the dragon, and slash through its scales.")
                    print("Dragon blood gushes out, and enters into your mouth. You remember a tale of dragon blood, that some could be poison, and some could turn a man into a god. My blood fealtsearing with pain. I screamed out in pain. This dragon, this dragon was special. Your muscles started growing. You felt like you could hold the world in one hand. The dragon blood had turned you into a god. What do you do? A. Run at the dragon, B. Grab the dragon")
                    answer_4_1_1 = (input("Put answer here: "))
                    if answer_4_1_1 == a_1:
                        print("You run at the dragon with all of your force.")
                        print("You slam it into the side of the mountain. It hurls in pain. You punch it through the mountain. Its head becomes the mountain. You walk back down into town, feeling like a god. You had just saved the town. GG. You were written in the history books, as a god, a legend among men, you were, The Warrior of Burdengur.")
                        print(input("Type here to end the game"))
                        quit()
                    if answer_4_1_1 == b_1:
                        print("You grab the dragon by the throat. What do you do? A: Crush its throat, B: Slam it into the mountain. ")
                        answer_4_1_1_1 = (input("Put answer here: "))
                        if answer_4_1_1_1 == a_1:
                            print("You crush its throat. It heads exploads off, leaving you with more dragon blood. Do you A. Drink more, and risk your life, B. Return to the kingdom, being a hero.")
                            answer_4_1_1_1_1 = (input("Put answer here: "))
                            if answer_4_1_1_1_1 == a_1:
                                print("You drink the dragon blood, and die. Turns out, it wasnt a myth. It was just simple dragon info. You die, and people know you as the hero who sacraficed his life for the kingdom of burdengur. You've won, but at what cost?")
                                (input("Press any key to end: "))
                                quit()
                        if answer_4_1_1_1 == b_1:
                            print("You slam it into the side of the mountain. It hurls in pain. You punch it through the mountain. Its head becomes the mountain. You walk back down into town, feeling like a god. You had just saved the town. GG. You were written in the history books, as a god, a legend among men, you were, The Warrior of Burdengur.")
                            print(input("Type here to end the game"))
                            quit()
                if answer_4_1 == b_1:
                    print("You roll away.")
                    print("You feel the dragons fire brush against your skin. A tiny bit of your metal armor is searing hot. Do you A. Strike the dragon, B: Run away ")
                    answer_6 = (input("Put answer here: "))
                    if answer_6 == a_1:
                        print("You run at the dragon and slash through its scales")
                        print("Dragon blood gushes out, and enters into your mouth. You remember a tale of dragon blood, that some could be poison, and some could turn a man into a god. My blood fealtsearing with pain. I screamed out in pain. This dragon, this dragon was special. Your muscles started growing. You felt like you could hold the world in one hand. The dragon blood had turned you into a god. What do you do? A. Run at the dragon, B. Grab the dragon")
                        answer_4_1_1 = (input("Put answer here: "))
                        if answer_4_1_1 == a_1:
                            print("You run at the dragon with all of your force.")
                            print("You slam it into the side of the mountain. It hurls in pain. You punch it through the mountain. Its head becomes the mountain. You walk back down into town, feeling like a god. You had just saved the town. GG. You were written in the history books, as a god, a legend among men, you were, The Warrior of Burdengur.")
                            print(input("Type here to end the game"))
                            quit()
                        if answer_4_1_1 == b_1:
                            print("You grab the dragon by the throat. What do you do? A: Crush its throat, B: Slam it into the mountain. ")
                            answer_4_1_1_1 = (input("Put answer here: "))
                            if answer_4_1_1_1 == a_1:
                                print("You crush its throat. It heads exploads off, leaving you with more dragon blood. Do you A. Drink more, and risk your life, B. Return to the kingdom, being a hero.")
                                answer_4_1_1_1_1 = (input("Put answer here: "))
                                if answer_4_1_1_1_1 == a_1:
                                    print("You drink the dragon blood, and die. Turns out, it wasnt a myth. It was just simple dragon info. You die, and people know you as the hero who sacraficed his life for the kingdom of burdengur. You've won, but at what cost?")
                                    (input("Press any key to end: "))
                                    quit()
                        if answer_4_1_1_1 == b_1:
                            print("You slam it into the side of the mountain. It hurls in pain. You punch it through the mountain. Its head becomes the mountain. You walk back down into town, feeling like a god. You had just saved the town. GG. You were written in the history books, as a god, a legend among men, you were, The Warrior of Burdengur.")
                            print(input("Type here to end the game"))
                            quit()
                    if answer_6 == b_1:
                        print("You run down the mountain. You trip, and fall on the searing hot part of your sholder. You scream in pain. AS you tumble down the hill, the dragon comes after you, for an aftersnack. He grabs you with his teeth and-...")
                        print("He ate you. He went for the kingdom, and burnt it to a crisp. The few survivors knew you as the coward of burdengur. The one who destroyed the kingdom. The one, who failed the greatest task ever.")
                        (input("Press any key to end: "))
                        quit()

            if answer_4 == b_1:
                print("You go right.")
                print("You walk up a long flight of stairs. You see a group of goblins. What do you do? A: Attack, B: Run back down")
                answer_5 = (input("Put input here: "))
                if answer_5 == a_1:
                    print("You slash at one of the goblins. It gets destroyed. You slash at the other one and it gets demolished into bits and pieces.")
                    
        if answer_3 == b_1:
            print("You attempt to run away from the slimes, but trip and fall down the whole entire mountain. You were halfway up it! You fall down the mountain, land on the ground after falling a deathly long while, then die, becoming another one of the thousands of bones down at the beggining of the mountain. Great job. ")
            time.sleep(9)
            quit()
    if answer_2 == b_1:
        print("You run away, and fail your mission.")
        print('"You ran away, from a slime? We are now screwed! The kingdom of Burdengur is now doomed! You have doomed us all!" The kingdom gets burned to ashes, and you fail your mission.')
        time.sleep(7)
        quit()


if answer_1 == b_1:
    quit()







