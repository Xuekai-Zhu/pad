def solution():
    fuel_tank_cost = 45
    mileage_per_tank = 500
    total_mileage = 2000
    food_cost_ratio = 3/5
    

    # Calculate the number of times Mallory needed to refill the fuel tank
    num_refills = total_mileage // mileage_per_tank
    if total_mileage % mileage_per_tank != 0:
        num_refills += 1

    # Calculate the total cost of fuel for the trip
    fuel_cost = num_refills * fuel_tank_cost

    # Calculate the amount spent on food
    food_cost = food_cost_ratio * fuel_cost

    # Calculate the total amount spent on the trip
    total_cost = fuel_cost + food_cost
    result = total_cost

    return result

print(solution())