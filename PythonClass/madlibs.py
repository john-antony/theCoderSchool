
print("Welcome to Mad Libs!")

# Story template with blanks
story_template = "Once upon a time in a {adjective} {place}, there was a {noun} who loved to {verb}. One day, the {noun} {adverb} {verb} {preposition} a {adjective} {noun}. Everyone in {place} was {emotion}."

# Get words from the user
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
preposition = input("Enter a preposition: ")
emotion = input("Enter an emotion: ")

# Fill in the blanks with user input
filled_story = story_template.format(adjective=adjective, place=place, noun=noun, verb=verb, adverb=adverb, preposition=preposition, emotion=emotion)

# Display the completed story
print("\nHere's your Mad Libs story:\n")
print(filled_story)
