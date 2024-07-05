# 2. Quick Decisions: The Event Planner 🎉

# Objective: To practice the use of shorthand if statements.

# Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"
print(venue)

# Task 2: Venue Selection

# Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"
audio_video = ""
if venue == "large hall":
    audio_video = "audio system"
else:
    audio_video = "projector"
print(venue + " with " + audio_video)

# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

catering = input("Type of food to be catered")
type_of_food = "Veggie Deligh Caterers" if catering == "vegeterian" else "Gourmet Meals Caterers"
print(venue + " with " + audio_video + " and food catered from " + type_of_food)