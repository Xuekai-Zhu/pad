def solution():
    """Abel leaves for a vacation destination 1000 miles away driving 50 miles per hour. An hour later Alice leaves from the same point for the same destination, traveling 40 miles per hour. How much earlier does Abel reach the destination in minutes?"""
    # Define the total distance and the speeds of Abel and Alice
    total_distance = 1000
    abel_speed = 50
    alice_speed = 40

    # Calculate the time it takes Abel to reach the destination
    abel_time = total_distance / abel_speed

    # Calculate the time it takes Alice to reach the destination
    alice_time = (total_distance - 50) / alice_speed

    # Calculate the time difference in minutes
    time_difference = (abel_time - alice_time) * 60

    # Return the result
    result = round(time_difference)
    return result

print(solution())