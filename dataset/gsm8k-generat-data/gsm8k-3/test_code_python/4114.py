def solution():
    """Kristin can run three times faster than Sarith. If Kristin runs 12 times around the adult football field and Sarith runs at the same time around the children's football field that is half the distance as the other field, how many laps did Sarith go around the children's football field?"""
    # Define the ratio of Kristin's speed to Sarith's speed
    KRISTIN_SPEED_RATIO = 3

    # Define the number of laps Kristin ran
    kristin_laps = 12

    # Define the ratio of the distances of the two football fields
    FIELD_DISTANCE_RATIO = 2

    # Calculate the number of laps Sarith ran
    sarith_laps = kristin_laps * (KRISTIN_SPEED_RATIO + 1) / (FIELD_DISTANCE_RATIO + 1)

    # Display the number of laps Sarith ran
    result = sarith_laps
    return result

print(solution())