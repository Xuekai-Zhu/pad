def solution():
    """The difference between the ages of two friends is 2 years. The sum of their ages is 74 years. Find the age of the older friend."""
    # Use algebra to solve for the ages of the two friends
    # Let x be the age of the younger friend and x+2 be the age of the older friend
    # Then x + (x+2) = 74
    # Simplifying, we get 2x + 2 = 74, which gives us x = 36
    # So the age of the older friend is x+2 = 38

    age_younger = 36
    age_older = age_younger + 2

    # Display the age of the older friend
    result = age_older
    return result

print(solution())