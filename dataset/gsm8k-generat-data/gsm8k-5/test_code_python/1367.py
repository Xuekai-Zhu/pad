def solution():
    # Let x be the amount of funding at the lowest level
    # The funding at the second level is 10x
    # The funding at the highest level is 100x
    # The total funding received is 10x * 10 + 3 * 10x + 2 * 100x = 12000
    # Simplifying, we get 232x = 12000
    # Solving for x, we get x = 51.72
    # Therefore, the highest level of financial backing was 100x = $5172
    highest_level = 100 * 51.72
    result = highest_level
    return result

print(solution())