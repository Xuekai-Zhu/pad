def solution():
    """The journey from Abel's house to Alice's house is 35 miles and is divided into 5 equal portions. Abel is driving at a speed of 40 miles per hour. After traveling for 0.7 hours, how many portions of the journey has he covered?"""
    # Define the distance of each portion of the journey
    portion_distance = 35 / 5

    # Calculate the distance Abel has covered after 0.7 hours
    distance_covered = 40 * 0.7

    # Calculate the number of portions Abel has covered
    portions_covered = distance_covered / portion_distance

    # Display the number of portions covered
    result = portions_covered
    return result

print(solution())