# Challange: Create the output display for the PayUp app.

# 1. Check out the example output in 'example_output.md'
# 2. Define a variable for each item: event name, cost, service charge,
#    group size, grand total, and total per person. Use made-up values for now
#    we'll do the math later!
# 3. Build the display line by line using print and f-strings.
# Remember: an empty print() creates a blank line.
# 4. Run  it and make sure it matches the example.

# Variables 
event_name = "Tsunami "
cost = 300
service_charges = 30
group_size = 3
grand_total = cost + service_charges

total_for_each_person = grand_total / group_size

print("Welcome to PayUp!\n")
print(f"Here's the breakdown for dinner at {event_name}\n")
print(f"Cost: ${cost}")
print(f"Service charges: ${service_charges}")
print(f"Grand total: ${grand_total}\n")
print(f"Each person must PayUp: ${total_for_each_person}")