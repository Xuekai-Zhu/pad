def solution():
    current_savings = 28
    parking_cost = 10
    entrance_cost = 55
    meal_pass_cost = 25
    distance = 165
    mpg = 30
    gas_price = 3

    # Calculate the cost of gas for the round trip to Sea World
    gas_cost = (distance/mpg) * gas_price * 2

    # Calculate the total cost of the trip
    total_cost = parking_cost + entrance_cost + meal_pass_cost + gas_cost

    # Calculate how much more Sally needs to save up
    more_to_save = total_cost - current_savings
    result = more_to_save
    return result

print(solution())