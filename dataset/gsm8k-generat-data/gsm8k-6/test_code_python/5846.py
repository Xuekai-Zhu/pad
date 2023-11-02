def solution():
    # Calculate the weight John can front squat
    front_squat = 0.8 * 250  # John back squats 250 kg after increasing by 50 kg
    # Calculate the weight John can triple front squat
    triple_front_squat = 0.9 * front_squat
    # Calculate the total weight lifted for three triples
    total_weight_lifted = 3 * 3 * triple_front_squat  # John does three triples
    result = total_weight_lifted
    return result

print(solution())