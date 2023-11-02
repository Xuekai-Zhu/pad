def solution():
    """Mona bikes 30 miles each week to stay fit. This week, she biked on Monday, Wednesday, and Saturday. On Wednesday, she biked 12 miles. On Saturday, she biked twice as far as on Monday. How many miles did she bike on Monday?"""
    # Define the total distance biked and the distance biked on Wednesday
    total_distance = 30
    wednesday_distance = 12

    # Define the distance biked on Saturday in terms of the distance biked on Monday
    saturday_distance = 2 * monday_distance

    # Calculate the total distance biked on Monday, Wednesday, and Saturday
    # and solve for the distance biked on Monday
    monday_distance = (total_distance - wednesday_distance - saturday_distance) / 3

    # Return the distance biked on Monday
    result = monday_distance
    return result

print(solution())