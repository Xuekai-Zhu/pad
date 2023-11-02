def solution():
    """Luis is driving 80 miles in 2 hours. How far will he go in 15 minutes?"""
    # Convert 2 hours to minutes
    time = 2 * 60

    # Calculate Luis's speed (in miles/minute)
    speed = 80 / time

    # Calculate the distance Luis will travel in 15 minutes
    distance = speed * 15

    # Display the distance
    result = distance
    return result

print(solution())