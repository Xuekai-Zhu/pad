def solution():
    cherry_candies = None
    grape_candies = None
    apple_candies = None
    total_candies = None

    # Let's use algebra to solve this problem.
    # Let's assume the number of cherry candies is x.
    # Then the number of grape candies is 3x (since there are 3 times as many grape candies as cherry candies).
    # Then the number of apple candies is 2 * 3x = 6x (since there are 2 times as many apple candies as grape candies).

    # The total number of candies is x + 3x + 6x = 10x.
    # So we can divide the total cost by 10 to find the cost per candy.
    cost_per_candy = 200 / 10

    # Each candy costs $2.50, so we can divide the cost per candy by 2.5 to find the number of candies.
    cherry_candies = int(x)
    grape_candies = int(3 * x)
    apple_candies = int(6 * x)
    total_candies = cherry_candies + grape_candies + apple_candies

    # Return the number of grape candies.
    result = grape_candies
    return result

print(solution())