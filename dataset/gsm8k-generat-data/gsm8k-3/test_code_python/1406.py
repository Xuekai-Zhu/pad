def solution():
    """Bill is trying to count the toddlers at his daycare, but they keep running around. He double-counts 8 toddlers and misses 3 who are hiding. If Bill thinks he counted 26 toddlers, how many are there really?"""
    # Let x be the true number of toddlers
    # Bill double-counts 8, so he counts them as 2 each
    # He also misses 3 toddlers
    # Therefore, his count is x + 8 - 3*2 = x + 2
    # We know that his count is 26
    # Therefore, x + 2 = 26
    # Solving for x, we get:
    x = 24

    # Display the true number of toddlers
    result = x
    return result

print(solution())