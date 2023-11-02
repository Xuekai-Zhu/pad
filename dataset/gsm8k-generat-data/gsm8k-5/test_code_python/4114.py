def solution():
    # Calculate Kristin's speed relative to Sarith's speed
    relative_speed = 3

    # Calculate the number of laps Kristin runs on the adult football field
    kristin_laps = 12

    # Calculate the distance of the adult football field
    adult_field_distance = kristin_laps / relative_speed

    # Calculate the distance of the children's football field
    children_field_distance = adult_field_distance / 2

    # Calculate the number of laps Sarith runs on the children's football field
    sarith_laps = children_field_distance * relative_speed
    result = sarith_laps
    return result

print(solution())