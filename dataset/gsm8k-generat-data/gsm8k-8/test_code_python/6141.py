def solution():
    # Calculate the number of times the fuel tank needs to be refilled
    num_refills = 2000 // 500

    # Calculate the total cost of fuel for the whole journey
    fuel_cost = num_refills * 45

    # Calculate the amount spent on food, which is 3/5 of the fuel cost
    food_cost = (3/5) * fuel_cost

    # Calculate the total amount spent on the journey
    total_cost = fuel_cost + food_cost
    result = total_cost
    return result

print(solution())