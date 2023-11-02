def solution():
    """John can front squat 80% as much as he back squats.  He used to back squat 200 kg but increased that by 50 kg.  He can do a triple equal to 90% of the amount he front squats.  How much weight will he move if he does three triples?"""
    # Calculate John's front squat weight
    back_squat_weight = 200 + 50  # 250 kg after increasing by 50 kg
    front_squat_weight = back_squat_weight * 0.8

    # Calculate the weight for one set of three front squats
    triple_weight = front_squat_weight * 0.9 * 3

    # Calculate the weight for three sets of three front squats
    total_weight = triple_weight * 3

    # Display the total weight
    result = total_weight
    return result

print(solution())