def solution():
    # Calculate the weight Tom is holding in each hand 
    weight_in_hand = 1.5 * 150  # 1.5 times his weight 

    # Calculate the weight of the weight vest
    weight_vest = 0.5 * 150  # half his weight 

    # Calculate the total weight that Tom was moving with 
    total_weight = (2 * weight_in_hand) + weight_vest  # two hands and weight vest 

    result = total_weight
    return result

print(solution())