def solution():
    """The journey from Abel's house to Alice's house is 35 miles and is divided into 5 equal portions. Abel is driving at a speed of 40 miles per hour. After traveling for 0.7 hours, how many portions of the journey has he covered?"""
    # Define the length of the journey and the speed of Abel
    journey_length = 35
    abel_speed = 40

    # Calculate the length of each portion of the journey
    portion_length = journey_length / 5

    # Calculate the distance that Abel has covered after 0.7 hours
    distance_covered = abel_speed * 0.7

    # Calculate the number of portions covered by Abel
    portions_covered = distance_covered / portion_length

    result = round(portions_covered, 1)
    return result

print(solution())