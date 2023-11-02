def solution():
    """Mona bikes 30 miles each week to stay fit. This week, she biked on Monday, Wednesday, and Saturday. On Wednesday, she biked 12 miles. On Saturday, she biked twice as far as on Monday. How many miles did she bike on Monday?"""
    # Define the total distance biked in the week
    total_distance = 30

    # Calculate the distance biked on Wednesday
    wednesday_distance = 12

    # Calculate the total distance biked on Monday and Saturday
    monday_saturday_distance = total_distance - wednesday_distance

    # Calculate the distance biked on Saturday
    saturday_distance = monday_saturday_distance / 3 * 2

    # Calculate the distance biked on Monday
    monday_distance = monday_saturday_distance - saturday_distance

    # Display the distance biked on Monday
    result = monday_distance
    return result

print(solution())