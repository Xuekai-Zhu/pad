def solution():
    """A family of 12 monkeys collected 10 piles of bananas. 6 piles had 9 hands, with each hand having 14 bananas, while the remaining piles had 12 hands, with each hand having 9 bananas. How many bananas would each monkey get if they divide the bananas equally amongst themselves?"""
    # Calculate the total number of bananas in the 6 piles with 9 hands each
    bananas_6_piles = 6 * 9 * 14

    # Calculate the total number of bananas in the remaining piles with 12 hands each
    bananas_remaining_piles = 4 * 12 * 9

    # Calculate the total number of bananas collected by the family
    total_bananas = bananas_6_piles + bananas_remaining_piles

    # Calculate the number of bananas each monkey would get if they divide the bananas equally
    bananas_per_monkey = total_bananas / 12

    # return the result
    result = bananas_per_monkey
    return result

print(solution())