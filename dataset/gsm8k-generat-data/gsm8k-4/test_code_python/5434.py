def solution():
    """Kylie and Kayla pick apples together and take home 340 apples total. If Kayla picked 10 more than 4 times the amount of apples that Kylie picked, how many apples did Kayla pick?"""
    # Let's assume the number of apples picked by Kylie as x.
    x = None

    # Kayla picked 10 more than 4 times the amount of apples that Kylie picked
    y = 4 * x + 10

    # Total number of apples picked by Kylie and Kayla together is 340
    x + y = 340

    # Solving the equations
    x + (4*x+10) = 340
    5*x = 330
    x = 66

    # Therefore, Kayla picked
    y = 4*x + 10
    result = y
    return result

print(solution())