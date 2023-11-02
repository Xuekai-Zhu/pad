def solution():
    kristin_laps = 12
    sarith_speed_ratio = 1/3
    children_field_distance_ratio = 1/2

    # Calculate the distance of the adult football field
    adult_field_distance = kristin_laps

    # Calculate the distance of the children's football field
    children_field_distance = adult_field_distance * children_field_distance_ratio

    # Calculate the time it takes for Kristin to run 12 laps
    kristin_time = adult_field_distance / 12

    # Calculate the time it takes for Sarith to run the same distance as Kristin around the children's football field
    sarith_time = kristin_time / (1 + sarith_speed_ratio)

    # Calculate the number of laps Sarith can run in the time it takes Kristin to run 12 laps
    sarith_laps = (sarith_time / kristin_time) * 12

    result = sarith_laps
    return result

print(solution())