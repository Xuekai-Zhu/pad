def solution():
    # Calculate the cost of food
    food_cost = (3/5) * 45 * (2000/500)  # Mallory covers 2000 miles in total and needs to fill the tank 4 times (2000/500). The cost of fueling the car for the whole journey is 45*4 = 180. The cost of food is 3/5 of $180.

    # Calculate the total amount of money used
    total_cost = 180 + food_cost
    result = total_cost
    return result

print(solution())