def solution():
    grocery_store_distance = 8
    school_distance = 6
    soccer_practice_distance = 12
    total_distance = grocery_store_distance + school_distance + soccer_practice_distance + (2 * school_distance)

    car_mpg = 25
    gas_price = 2.5

    # Calculate how much gas Carla's car will use for the whole trip
    gas_used = total_distance / car_mpg

    # Calculate the total cost of gas for the trip
    total_gas_cost = gas_used * gas_price
    result = total_gas_cost
    return result

print(solution())