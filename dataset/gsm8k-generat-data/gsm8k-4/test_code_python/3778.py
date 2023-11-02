def solution():
    """A highway is being extended from its current length of 200 miles up to 650 miles. 50 miles are built on the first day, and three times this amount are built on the second day.  How many miles still need to be added to the highway to finish extending it?"""
    # Define the current length and the target length of the highway
    current_length = 200
    target_length = 650

    # Build 50 miles on the first day
    current_length += 50

    # Build three times as much on the second day
    current_length += 3 * 50

    # Calculate the remaining distance to build
    remaining_distance = target_length - current_length

    # return the result
    result = remaining_distance
    return result

print(solution())