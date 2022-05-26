words = ["Allegory", "Alliteration", "Allusion", "Anagram", "Analogy", "Antagonist",
			"Anti-hero", "Anthropomorphism", "Antithesis", "Apostrophe", "Archetype", 
			"Atmosphere", "Catharsis", "Caricature", "Cliche", "Cliffhanger", "Character (dynamic)",
			"Character (static)", "Cliamx", "Conflict", "Connotation", "Dark Comedy", "Denotation",
			"Dystopia", "Epithet", "Euphemism", "Flashforward", "Flashback", "Foil", "Foreshadowing",
			"Genre", "Hubris", "Hyperbole", "Idiom", "Imagery", "Internal Rhyme", "Irony (Verbal)", 
			"Irony (Situational)", "Irony (Dynamic)", "Kenning", "Malapropism", "Metaphor"]

definitions = ["Where characters or events in a story represent ideas and concepts",
					"Repetition of an initial consonant sound, in poetry",
					"Figure of speech where the author refers to a subject in a passing reference, it's up to the reather to make a connection",
					"Literary device where the writer jumbles up parts of a word to create a new word (rearrange letters)",
					"a comparison between two things for the purpose of explanation or clarification", 
					"a character or an institution that opposes the protagonist or main character",
					"a central character who lacks conventional heroic qualities, they blur the line between hero and villain",
					"when a human quality, emotion or ambition is given to a nonhuman object or being", 
					"when the writer puts two sentences of contrasting meanings close to one another",
					"a figure of speech in which the speaker addresses an object concept or an absent person that is unable to respond",
					"a concept, person, or object that has served as a universally understood prototype of its kind",
					"it's created with the setting or scene elicits and emotional response in the reader/viewer",
					"the process of releasing and thereby providing relief form stronger or repressed emotions, usually felt by the audience while exposed to a story that brings out great sorrow, pity or laughter",
					"a simple image show me the features of its object in a simplified or exaggerated way",
					"an expression, idea, or element which has become overused to the point of losing its original meaning",
					"a plot device in fiction which features the main character in a precarious or difficult dilemma at the end of an episode of serialized fiction. It's used to ensure the audience will return to see how they resolve the dilemma",
					"it goes through change or growth in the history",
					"it remains the same through the story and does not experience change",
					"a part of any basic plot line it is the most exciting or intense part of the story",
					"it's the struggle between opposing forces",
					"a word that has it, has an addition to its straightforward dictionary meaning, another meaning, it can be formulated as a series of qualities, contexts, and emotional responses associated with it",
					"it's a comical work that uses black humour which makes light of an otherwise solemn subject or matter",
					"the literal meaning of a word",
					"and imagined setting where everything is unpleasant or bad. This could be a totalitarian, apocalyptic, or environmentally degraded society",
					"it's a descriptive device used to add to a person's or place's regular name and attribute some special quality to it.(Alexander the Great)",
					"this term is used to refer to the use of a comparatively mild or or less harsh of a negative description instead of his original form. It's used to write about matters that are uncomfortable or embarrassing",
					"literary or cinematic device in which later events interrupt the normal chronological order of a narrative. This device is often used to give importance about what may happen later in the plot",
					"the opposite of a flash forward",
					"a literary device where the author creates a character whose primary purpose is to create a contrast to another character by laying emphasis or drawing attention to the differences",
					"the use of words or places that give hints to the reader of some thing that is going to happen without revealing the story or spoiling the suspense. It's used to suggest an upcoming outcome of the story",
					"a category of artistic composition as in music or literature. Characterized by similarities in form, style, or subject matter",
					"another way of saying overly arrogant, they have a false belief that they are untouchable and they allow reality to sleep away from them",
					"it's an exaggeration in writing used for effect",
					"an expression that is peculiar to itself grammatically or cannot be understood from the individual meanings of its elements but is understood by most people",
					"a strong device for the author creates a mental image for the reader using the five senses. It helps the reader to visualize an experience the authors writing.",
					"a practice of forming a rhyme and only one line of verse, it's also known as the middle rhyme",
					"it's similar to sarcasm and it occurs when a writer makes a statement in which the means something different than what they appear to be",
					"it occurs when the reader is led to believe that the thing will occur, when in fact, the opposite occurs",
					"it occurs when the reader or audience knows something, but the characters within the story do not",
					"it's characteristically related to works in old English poetry where the author will create a new poetic compound phrase to describe a familiar person, place, or idea",
					"it refers to the practice of substituting words with similar sounding words that have different meanings. This often leads to a situation of confusion, misunderstanding, and amusement",
					"it's an implied comparison between two unlike things that actually have something in common"]



#Copyright 2022, Yicheng Xia, All rights reserved

import random


mode = int(input("Which mode do you want to play? 1 for definition to word, 2 for word to defition "))
if mode != 1 and mode != 2:
	print("wrong answer")

print("You can always type \"quit\" to quit the game and get your score")

running = True
score = 0

if mode == 1:
	while running:
		print("==================================================")
		index = random.choice(range(0, len(words)))
		prompt = f"Which word does this definition relate to? \n------------\n{definitions[index]}\n------------\n"
		answer = input(prompt)

		if answer.lower() == "quit":
			print(f"Your final score was {score}")
			running = False;
			break

		if answer.lower() == words[index].lower():
			print("Correct! you got 1 point\n")
			score += 1
		else:
			print("Wrong!")
			print(f"The correct answer was {words[index]}\n")

		print("==================================================")
elif mode == 2:
	while running:
		print("==================================================")
		index = random.choice(range(0, len(words)))
		prompt = f"Which definition does this word relate to? \n------------\n{words[index]}\n------------\n"
		answer = input(prompt)

		if answer.lower() == "quit":
			print(f"Your final score was {score}")
			running = False;
			break

		print(f"The correct answer was: {definitions[index]}")
		point = input("Would you consider that you got the answer right? (yes/no)").lower();

		if point == "yes":
			score += 1
			print("Congratulations, you got 1 point!\n")
		elif point == "no":
			print("F\n")



		print("==================================================")
else:
    pass

