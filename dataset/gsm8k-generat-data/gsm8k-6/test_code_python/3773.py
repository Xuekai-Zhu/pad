def solution():
    # Calculate the number of sweets Aaron eats
    eaten_sweets = (30 + 40 + 50) * (1/2)  # Aaron eats half of each flavored sweet

    # Calculate the number of sweets left after Aaron gives 5 cherry-flavored sweets to his friend
    remaining_sweets = (30 - 5) + (40 * 0.5) + (50 * 0.5)  # Aaron gives 5 cherry-flavored sweets to his friend and eats half of each other flavored sweet

    result = remaining_sweets
    return result

print(solution())