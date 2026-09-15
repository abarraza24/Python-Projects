#breakfast = "pancakes "
#lunch = "salad "
#dinner = "pizza "

# Adding strings together are called concatenating strings
#meal_plan = breakfast + lunch + dinner
#print(f"My current meal plan {meal_plan}")

# Challange 1 - Daily Planner
# Print a sentance that outlines your plan today

# 1. Make three variables: morning, afternoon, and evening.
# 2. To each variable, save a string containing one activity (taking a nap, skiing, etc)
# 3. Add each variable together and save to a variable called 'plan_for_today'

# Here's an example of what your output should look like:
# "My plan for today is: 1.drink coffee 2. study python 3.dance party"
# Use f'strings


morning = "Hitting the Gym "
afternoon = "Going to Java class "
night = "Meal prepping "

plan_for_today = morning + afternoon + night
print(f"My plan for today is 1. {morning} 2. {afternoon} 3. {night}\n\n")

# Challange: Excuse Generator
# Don't feel like going out tonight? Write a program that generates excuses for why you have to stay
# in.

#1. Define these variables: first_name, event, number, noun, and verb.
# Use whatever values you want, as long as they match the format.
# Write an f-strig using your variables that generates a one-sentence excuse.
# For example "Sorry [Pedro], I can't go to the [movies] - I have [345] [bees] to [crochet] and
# Its taking longer than expected."

first_name = "Pedro"
event = "Rave"
number = 117
noun = "class"
verb = "run"

my_excuse = f"Sorry {first_name}, I can't go to the {event} - I have {number} {noun} to {verb} too."
print(my_excuse)