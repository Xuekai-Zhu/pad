def solution():
    """John can front squat 80% as much as he back squats. He used to back squat 200 kg but increased that by 50 kg. He can do a triple equal to 90% of the amount he front squats. How much weight will he move if he does three triples?"""
    # Define the initial weight John back squatted and the amount he increased it by
    initial_weight_back_squat = 200
    increased_weight_back_squat = 50
    final_weight_back_squat = initial_weight_back_squat + increased_weight_back_squat

    # Calculate the weight John can front squat
    front_squat_weight = 0.8 * final_weight_back_squat

    # Calculate the weight John can triple front squat
    triple_front_squat_weight = 0.9 * front_squat_weight

    # Calculate the total weight John moves if he does three triples
    total_weight = triple_front_squat_weight * 3

    result = total_weight
    return result

print(solution())