def solution():
    kitchen_cost = 20000
    bathroom_cost = 12000
    other_cost_per_sqft = 100
    total_sqft = 2000
    num_kitchens = 1
    kitchen_sqft = 400
    num_bathrooms = 2
    bathroom_sqft = 150

    # Calculate the total cost of the kitchen module
    total_kitchen_cost = kitchen_cost * num_kitchens

    # Calculate the total cost of the bathroom modules
    total_bathroom_cost = bathroom_cost * num_bathrooms

    # Calculate the total cost of all other modules
    other_sqft = total_sqft - (num_kitchens * kitchen_sqft) - (num_bathrooms * bathroom_sqft)
    total_other_cost = other_sqft * other_cost_per_sqft

    # Calculate the total cost of the modular home
    total_cost = total_kitchen_cost + total_bathroom_cost + total_other_cost
    result = total_cost
    return result

print(solution())