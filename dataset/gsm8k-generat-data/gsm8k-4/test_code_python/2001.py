def solution():
    """Jenna is on a road trip. She drives for 2 hours at 60mph. She takes a bathroom break, and then she continues driving for 3 hours at 50 mph. She can drive for 30 miles on one gallon of gas. If one gallon of gas costs $2, how much money does she spend on gas for her trip?"""
    # Calculate the distance Jenna drove during each leg of her trip
    distance_leg1 = 2 * 60
    distance_leg2 = 3 * 50

    # Calculate the total distance Jenna drove
    total_distance = distance_leg1 + distance_leg2

    # Calculate the total amount of gas Jenna used
    total_gas = total_distance / 30

    # Calculate the total cost of gas used
    total_cost = total_gas * 2

    # return the result
    result = total_cost
    return result

print(solution())