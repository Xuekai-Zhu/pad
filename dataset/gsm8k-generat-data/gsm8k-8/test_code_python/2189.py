def solution():
    tom_weight = 150
    hand_weight = 1.5 * tom_weight
    vest_weight = 0.5 * tom_weight

    total_weight = tom_weight + 2 * hand_weight + vest_weight
    result = total_weight
    return result

print(solution())