def solution():
    first_leg_time = 2
    first_leg_speed = 60
    second_leg_time = 3
    second_leg_speed = 50
    gas_mileage = 30
    gas_price = 2.0

    # Calculate the distance Jenna covers on the first leg of her trip
    first_leg_distance = first_leg_time * first_leg_speed

    # Calculate the distance Jenna covers on the second leg of her trip
    second_leg_distance = second_leg_time * second_leg_speed

    # Calculate the total distance Jenna covers on her trip
    total_distance = first_leg_distance + second_leg_distance

    # Calculate the total amount of gas Jenna needs for the trip
    total_gas = total_distance / gas_mileage

    # Calculate the total cost of gas for the trip
    total_gas_cost = total_gas * gas_price
    result = total_gas_cost
    return result

print(solution())