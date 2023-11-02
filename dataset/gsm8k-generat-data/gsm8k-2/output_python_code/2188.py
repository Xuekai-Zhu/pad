def solution():
    """Tom weighs 150 kg. He manages to hold 1.5 times his weight in each hand while wearing a weight vest weighing half his weight. How much total weight was he moving with?"""
    tom_weight = 150
    hand_weight = 1.5 * tom_weight
    vest_weight = 0.5 * tom_weight
    total_weight = hand_weight * 2 + vest_weight
    result = total_weight
    return result

print(solution())