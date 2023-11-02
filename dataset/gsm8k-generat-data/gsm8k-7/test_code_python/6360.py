def solution():
    num_people = 3
    cost_per_meal = 10
    total_spent = 45

    # Calculate the total cost of all meals
    total_meal_cost = num_people * cost_per_meal

    # Calculate the cost of all ice cream scoops
    ice_cream_cost = total_spent - total_meal_cost

    # Calculate the cost of a single ice cream scoop
    cost_per_ice_cream = ice_cream_cost / num_people
    result = cost_per_ice_cream
    return result

print(solution())