def solution():
    """Three plastic chairs cost as much as a portable table. Five plastic chairs cost $55. If Manny wants to buy one portable table and two chairs, how much will be left in his $100?"""
    # First, we need to find the cost of one plastic chair and one portable table
    # Let's assume that the cost of one plastic chair is x and the cost of one portable table is y
    # Then, we can set up two equations based on the given information
    # Equation 1: 3x = y
    # Equation 2: 5x + y = 55
    # We can use equation 1 to substitute y in equation 2
    # 5x + 3x = 55
    # 8x = 55
    # x = 6.875
    # Now, we can find y using equation 1
    # y = 3x = 20.625
    # Manny wants to buy one portable table and two chairs, so the total cost would be 2x + y = 34.375
    # Manny has $100, so he would have 100 - 34.375 = 65.625 left
    result = 100 - (2*6.875 + 20.625)
    return result

print(solution())