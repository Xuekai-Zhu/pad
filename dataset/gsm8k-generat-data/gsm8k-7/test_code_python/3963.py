def solution():
    current_age = None

    # We can set up an equation based on the given information
    # Let x be John's current age
    # Then, 9 years from now, he will be x + 9
    # And 11 years ago, he was x - 11
    # So we have the following equation:
    # x + 9 = 3(x - 11)

    # Solving for x, we get:
    # x + 9 = 3x - 33
    # 42 = 2x
    # x = 21

    current_age = 21
    result = current_age
    return result

print(solution())