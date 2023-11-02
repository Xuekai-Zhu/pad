def solution():
    """Bob drove for one and a half hours at 60/mph. He then hit construction and drove for 2 hours at 45/mph. How many miles did Bob travel in those 3 and a half hours?"""
    # Calculate the distance traveled during the first leg of the trip
    distance_1 = 60 * 1.5

    # Calculate the distance traveled during the second leg of the trip
    distance_2 = 45 * 2

    # Calculate the total distance traveled
    total_distance = distance_1 + distance_2

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())