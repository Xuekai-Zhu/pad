def solution():
    # Calculate John's back squat weight after increasing by 50kg
    back_squat_weight = 200 + 50

    # Calculate John's front squat weight
    front_squat_weight = 0.8 * back_squat_weight

    # Calculate the weight John can triple front squat
    triple_weight = 0.9 * front_squat_weight

    # Calculate the total weight moved in three triples
    total_weight = triple_weight * 3

    result = total_weight
    return result

print(solution())