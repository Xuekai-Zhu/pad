def solution():
    """Jace drives 60 miles per hour. If Jace drives for 4 hours straight, take a 30-minute break, and then drives for another 9 hours straight, how many miles will he travel?"""
    # Define Jace's speed
    speed = 60

    # Calculate the distance Jace travels in the first 4 hours
    distance_1 = speed * 4

    # Calculate the distance Jace travels in the next 9 hours (minus the 30-minute break)
    distance_2 = (speed * 9) - (speed * 0.5)

    # Calculate the total distance traveled
    total_distance = distance_1 + distance_2

    # Return the result
    result = total_distance
    return result

print(solution())