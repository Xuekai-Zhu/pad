def solution():
    """Jim ran 16 miles in 2 hours while Frank ran 20 miles in 2 hours. How many more miles did Frank run than Jim in an hour?"""
    # Calculate the distance each person ran per hour
    jim_distance = 16 / 2
    frank_distance = 20 / 2

    # Calculate the difference in distance between Frank and Jim
    distance_diff = frank_distance - jim_distance

    # Return the difference in distance
    result = distance_diff
    return result

print(solution())