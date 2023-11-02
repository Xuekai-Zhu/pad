def solution():
    # Calculate the total number of bananas in the 6 piles with 9 hands each
    bananas_in_6_piles = 6 * 9 * 14

    # Calculate the total number of bananas in the remaining 4 piles with 12 hands each
    bananas_in_4_piles = 4 * 12 * 9

    # Calculate the total number of bananas collected
    total_bananas = bananas_in_6_piles + bananas_in_4_piles

    # Calculate the number of bananas each monkey would get if they divide the bananas equally
    bananas_per_monkey = total_bananas / 12

    result = bananas_per_monkey
    return result

print(solution())