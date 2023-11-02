def solution():
    """Tom weighs 150 kg. He manages to hold 1.5 times his weight in each hand while wearing a weight vest weighing half his weight. How much total weight was he moving with?"""
    weight = 150
    hand_weight = weight * 1.5
    vest_weight = weight * 0.5
    total_weight = (hand_weight * 2) + vest_weight
    result = total_weight
    return result

print(solution())