def solution():
    """The total distance between 2 towns is 200 miles. Roger and his friend drove 1/4 of the total distance, taking 1 hour to do so. They take lunch for another 1 hour and then drove the remaining distance going at the same speed as before. What's the total amount of time, in hours, Roger and his friend took to travel between the two towns?"""
    # Define the total distance
    total_distance = 200

    # Calculate the distance traveled during the first part of the trip
    first_distance = total_distance / 4

    # Calculate the time taken to travel the first distance
    first_time = 1

    # Calculate the time taken for lunch
    lunch_time = 1

    # Calculate the distance remaining after lunch
    remaining_distance = total_distance - first_distance

    # Calculate the time taken to travel the remaining distance
    remaining_time = remaining_distance / (first_distance / first_time)

    # Calculate the total time taken
    total_time = first_time + lunch_time + remaining_time

    # Display the total time taken
    result = total_time
    return result

print(solution())