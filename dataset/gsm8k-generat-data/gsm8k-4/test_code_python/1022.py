def solution():
    """Rachel is 4 years older than Leah. If the sum of their ages is 34, how old is Rachel?"""
    # Define the age difference between Rachel and Leah
    age_difference = 4

    # Set up the system of equations based on the given information
    # r = l + 4   (Rachel is 4 years older than Leah)
    # r + l = 34  (The sum of their ages is 34)

    # Substitute the first equation into the second to eliminate r
    # (l + 4) + l = 34
    # 2l + 4 = 34
    # 2l = 30
    # l = 15

    # Use the first equation to find Rachel's age
    r = 15 + 4

    result = r
    return result

print(solution())