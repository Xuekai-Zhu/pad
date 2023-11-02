def solution():
    """Jenna is on a road trip. She drives for 2 hours at 60mph. She takes a bathroom break, and then she continues driving for 3 hours at 50 mph. She can drive for 30 miles on one gallon of gas. If one gallon of gas costs $2, how much money does she spend on gas for her trip?"""
    # Calculate the distance Jenna drove in the first 2 hours
    distance1 = 60 * 2

    # Calculate the distance Jenna drove in the next 3 hours
    distance2 = 50 * 3

    # Calculate the total distance Jenna drove
    total_distance = distance1 + distance2

    # Calculate the number of gallons of gas Jenna used
    gas_used = total_distance / 30

    # Calculate the total cost of the gas used
    gas_cost = gas_used * 2

    # Display the total cost of the gas used
    result = gas_cost
    return result

print(solution())