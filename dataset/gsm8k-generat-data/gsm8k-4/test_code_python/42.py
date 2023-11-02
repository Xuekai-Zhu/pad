def solution():
    """A family of 12 monkeys collected 10 piles of bananas. 6 piles had 9 hands, with each hand having 14 bananas, while the remaining piles had 12 hands, with each hand having 9 bananas. How many bananas would each monkey get if they divide the bananas equally amongst themselves?"""
    # Calculate the total number of bananas collected
    num_bananas = (6 * 9 * 14) + (4 * 12 * 9)

    # Calculate the number of bananas each monkey would get if they divide them equally
    bananas_per_monkey = num_bananas / 12

    result = bananas_per_monkey
    return result

print(solution())