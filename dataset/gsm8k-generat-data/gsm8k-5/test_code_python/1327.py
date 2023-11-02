def solution():
    # Distance traveled on the first swing
    first_swing_distance = 180

    # Distance traveled on the second swing
    second_swing_distance = first_swing_distance / 2
    # Total distance after the second swing
    total_distance_after_second_swing = first_swing_distance + second_swing_distance + 20

    # Distance traveled on the third swing
    third_swing_distance = total_distance_after_second_swing - 20

    # Total distance from the starting tee to the hole
    total_distance = first_swing_distance + second_swing_distance + third_swing_distance
    result = total_distance
    return result

print(solution())