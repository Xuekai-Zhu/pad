def solution():
    """The cost of filling a car fuel tank is $45, and this can take you 500 miles before refilling. Mallory was going to her grammy's house, 2000 miles away. If she used 3/5 times as much money on food as she spent on filling the car fuel tank for the whole journey, calculate the total amount of money she used."""
    fuel_cost = 45
    fuel_distance = 500
    total_distance = 2000
    refills_needed = total_distance / fuel_distance
    total_fuel_cost = fuel_cost * refills_needed
    
    food_cost = (3/5) * fuel_cost
    total_food_cost = fuel_cost * refills_needed * food_cost
    
    total_cost = total_fuel_cost + total_food_cost
    result = total_cost
    return result

print(solution())