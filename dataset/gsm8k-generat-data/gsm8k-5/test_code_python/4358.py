def solution():
    num_pizzas = 5 # The mother bought 5 pizzas
    num_children = 20 # There are 20 children at the party
    possible_slices = [6, 8, 10] # The mother can choose to divide each pizza into 6, 8, or 10 slices

    # Loop through all possible slice options and find the one that results in an equal distribution
    for slices in possible_slices:
        total_slices = num_pizzas * slices # Calculate the total number of slices with this option
        if total_slices % num_children == 0: # If the total slices evenly divides among the children, return the number of slices
            result = slices
            return result

Question: A car rental company charges $25 per day or $0.20 per mile to rent a car. Sarah rented a car for 5 days and drove 500 miles. What is the total cost of her rental?
Solution:
def solution():
    days_rented = 5 # Sarah rented the car for 5 days
    miles_driven = 500 # Sarah drove 500 miles
    cost_per_day = 25 # The car rental company charges $25 per day
    cost_per_mile = 0.20 # The car rental company charges $0.20 per mile

    # Calculate the total rental cost based on the number of days rented and miles driven
    total_cost = (days_rented * cost_per_day) + (miles_driven * cost_per_mile)
    result = total_cost
    return result

print(solution())