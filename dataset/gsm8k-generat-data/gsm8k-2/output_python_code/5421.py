def solution():
    """There are 3 numbers that are consecutive integers. Together they have a sum of 18. What is the largest of the 3 numbers?"""
    # Let x be the smallest consecutive integer
    # Then the sum of the three consecutive integers is x + (x+1) + (x+2)
    # We know that the sum of the three consecutive integers is 18
    # So, we can write the equation: x + (x+1) + (x+2) = 18
    # Simplifying this equation, we get: 3x + 3 = 18
    # Solving for x, we get: x = 5
    # Therefore, the three consecutive integers are 5, 6, and 7
    # The largest of these three numbers is 7
    result = 7
    return result

print(solution())