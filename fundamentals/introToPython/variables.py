#meal_total = 100
#print (f"Total for meal: ${meal_total}")

# Challange 

# 1. Think of the last time you ate at a restaurant. How many people were you with ?
# 2. Save the number to a variable called my_party.
# 3. Turns out two more people showed up. Update my_party and print it again.

#my_party = 4
#print(f"There's {my_party} people in my party.")

#my_party = 6
#print(f"Sorry! There's two more people in my party making it {my_party} people in my party.")

# Variables in action.
#tip = 15 
# add total with tip
#print(meal_total + tip)

# Or better yet assigned it to a grand_total
#grand_total = meal_total + tip
#print(f"The total for this meal is ${grand_total}.")

#Python variables are snake_case

# Challange number 2
# 1. You and your friends just had dinner. Save the cost of the food to a variable called
# food_total
# 2. Save the cost of the drinks to a separate variable called drinks_total.
# 3. Add them together and save the result to a variable called meal_total.
# 4. Print meal_total
# 5. One friend didn't drink. Reduce drinks_total by whatever amount makes sense,
# and print meal_total again. Did it update?

food_total = 40
drinks_total = 17
meal_total = food_total + drinks_total

print(f"Total for meal ${meal_total}")

drinks_total = 7
meal_total = food_total + drinks_total

print(f"Updated Total for meal ${meal_total}")


