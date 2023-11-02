def solution():
    num_monkeys = 12
    num_piles = 10
    bananas_per_hand_in_small_piles = 14
    hands_per_small_pile = 9
    bananas_per_hand_in_big_piles = 9
    hands_per_big_pile = 12

    # Calculate the total number of bananas in the small piles
    total_bananas_in_small_piles = bananas_per_hand_in_small_piles * hands_per_small_pile * 6

    # Calculate the total number of bananas in the big piles
    total_bananas_in_big_piles = bananas_per_hand_in_big_piles * hands_per_big_pile * 4

    # Calculate the total number of bananas collected
    total_bananas = total_bananas_in_small_piles + total_bananas_in_big_piles

    # Calculate the number of bananas each monkey will get
    bananas_per_monkey = total_bananas / num_monkeys
    result = bananas_per_monkey
    return result

print(solution())