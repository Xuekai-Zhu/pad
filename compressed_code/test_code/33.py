def solution():
    
    monkey_count = 12
    pile_count = 10
    bananas_per_hand_1 = 14
    hands_per_pile_1 = 9
    bananas_per_hand_2 = 9
    hands_per_pile_2 = 12
    total_bananas_1 = bananas_per_hand_1 * hands_per_pile_1 * 6
    total_bananas_2 = bananas_per_hand_2 * hands_per_pile_2 * 4
    total_bananas = total_bananas_1 + total_bananas_2
    bananas_per_monkey = total_bananas / monkey_count
    result = bananas_per_monkey
    return result

print(solution())