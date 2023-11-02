def solution():
    # Calculate the total number of bananas collected
    bananas_in_6_piles = 6 * 9 * 14  # 6 piles had 9 hands, with each hand having 14 bananas
    bananas_in_remaining_piles = (10 - 6) * 12 * 9  # remaining piles had 12 hands, with each hand having 9 bananas
    total_bananas = bananas_in_6_piles + bananas_in_remaining_piles

    # Divide the bananas equally amongst the 12 monkeys
    bananas_per_monkey = total_bananas / 12
    result = bananas_per_monkey
    return result

print(solution())