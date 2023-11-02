def solution():
    fuel_cost = 45  # cost of filling the fuel tank
    fuel_distance = 500  # distance the car travels on a full tank
    total_distance = 2000  # total distance to be covered

    # Calculate the number of times the tank needs to be refilled
    num_refills = total_distance // fuel_distance

    # Calculate the total cost of fuel for the trip
    total_fuel_cost = num_refills * fuel_cost

    # Calculate the amount spent on food
    food_cost = (3/5) * fuel_cost
    total_food_cost = num_refills * food_cost

    # Calculate the total amount spent
    total_cost = total_fuel_cost + total_food_cost
    result = total_cost
    return result

print(solution())