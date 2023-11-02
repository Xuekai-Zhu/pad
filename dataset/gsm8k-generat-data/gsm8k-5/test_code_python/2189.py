def solution():
    tom_weight = 150  # Tom weighs 150 kg
    weight_in_each_hand = 1.5 * tom_weight  # Tom can hold 1.5 times his weight in each hand
    weight_vest = tom_weight / 2  # Tom's weight vest weighs half his weight

    # Calculate the total weight Tom was moving with
    total_weight = weight_in_each_hand * 2 + weight_vest
    result = total_weight
    return result

print(solution())