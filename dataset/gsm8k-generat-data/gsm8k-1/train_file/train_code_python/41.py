def solution():
    """A family of 12 monkeys collected 10 piles of bananas. 6 piles had 9 hands, with each hand having 14 bananas, while the remaining piles had 12 hands, with each hand having 9 bananas. How many bananas would each monkey get if they divide the bananas equally amongst themselves?"""
    monkey_count = 12
    hand_count_in_pile1 = 9
    hand_count_in_pile2 = 12
    banana_count_in_hand1 = 14
    banana_count_in_hand2 = 9

    total_bananas = (6 * hand_count_in_pile1 * banana_count_in_hand1) + (4 * hand_count_in_pile2 * banana_count_in_hand2)
    bananas_per_monkey = total_bananas // monkey_count
    
    result = bananas_per_monkey
    return result

print(solution())