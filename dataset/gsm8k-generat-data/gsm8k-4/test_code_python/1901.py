def solution():
    """The total distance between 2 towns is 200 miles. Roger and his friend drove 1/4 of the total distance, taking 1 hour to do so. They take lunch for another 1 hour and then drove the remaining distance going at the same speed as before. What's the total amount of time, in hours, Roger and his friend took to travel between the two towns?"""
    # Define the total distance
    total_distance = 200

    # Define the distance traveled in the first leg
    first_leg_distance = total_distance / 4

    # Define the time taken to travel the first leg
    first_leg_time = 1

    # Define the time taken for lunch
    lunch_time = 1

    # Define the speed of travel for the second leg
    second_leg_speed = first_leg_distance / first_leg_time

    # Define the distance traveled in the second leg
    second_leg_distance = total_distance - first_leg_distance

    # Define the time taken to travel the second leg
    second_leg_time = second_leg_distance / second_leg_speed

    # Calculate the total time taken for the trip
    total_time = first_leg_time + lunch_time + second_leg_time

    # Return the result
    result = total_time
    return result

print(solution())