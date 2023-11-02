def solution():
    """After eating half of the number of fruits he had, Martin remained with twice as many oranges as limes. If he has 50 oranges now, how many fruits did he initially have?"""
    # Let's assume that Martin initially had "x" number of fruits
    # He ate half, so he is left with "x/2" number of fruits
    # Let's assume that he had "y" number of limes initially
    # Then he had "x/2 - y" number of oranges initially
    # It is given that he is now left with 50 oranges, which is twice the number of limes he has now
    # So, 50 = 2 * (x/2 - y)
    # Simplifying the above equation, we get:
    # x/2 - y = 25
    # Also, he initially had x number of fruits, so
    # x = y + x/2 - y + 50
    # Simplifying the above equation, we get:
    # x = 100

    # Therefore, Martin initially had 100 fruits
    result = 100
    return result

print(solution())