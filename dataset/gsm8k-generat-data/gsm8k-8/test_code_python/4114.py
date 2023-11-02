def solution():
    # Define the ratio of Kristin's speed to Sarith's speed
    kristin_to_sarith_ratio = 3

    # Define the number of laps Kristin runs around the adult football field
    kristin_laps = 12

    # Calculate the distance ratio between the two football fields
    distance_ratio = 2

    # Calculate the number of laps Sarith runs around the children's football field
    sarith_laps = kristin_laps * (kristin_to_sarith_ratio * distance_ratio)

    result = sarith_laps
    return result

print(solution())