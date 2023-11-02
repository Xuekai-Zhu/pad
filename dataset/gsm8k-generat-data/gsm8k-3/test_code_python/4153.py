def solution():
    """When Hannah was 6 years old, her age was double the age of her sister July. Now, 20 years later, if July's husband is 2 years older than her, how old is he?"""
    # Let x be July's age now
    # Hannah's age now is x + 20
    # Hannah's age when she was 6 was x + 14 (20 years ago she was 6)
    # According to the problem, x + 14 = 2(x - 6)
    # Solving for x, we get x = 34
    # July's husband's age is x + 2 = 36

    july_age = 34
    husband_age = july_age + 2

    # Display July's husband's age
    result = husband_age
    return result

print(solution())