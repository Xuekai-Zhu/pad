def solution():
    """Kristin can run three times faster than Sarith. If Kristin runs 12 times around the adult football field and Sarith runs at the same time around the children's football field that is half the distance as the other field, how many laps did Sarith go around the children's football field?"""
    # Define the ratio of Kristin's speed to Sarith's speed
    KRISTIN_SPEED_RATIO = 3

    # Define the number of laps Kristin ran
    kristin_laps = 12

    # Calculate the total distance Kristin ran
    kristin_distance = kristin_laps * 1

    # Calculate the distance of each lap Kristin ran
    kristin_lap_distance = kristin_distance / kristin_laps

    # Calculate Sarith's speed
    sarith_speed = kristin_lap_distance / KRISTIN_SPEED_RATIO

    # Calculate the number of laps Sarith ran on the children's football field
    sarith_laps = (0.5 * kristin_laps * KRISTIN_SPEED_RATIO) / sarith_speed

    result = sarith_laps
    return result

print(solution())