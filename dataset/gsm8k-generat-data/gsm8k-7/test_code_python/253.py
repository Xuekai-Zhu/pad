def solution():
    # Let x be the length of the short side of the fence
    x = 1

    # The long sides are three times the length of the short side, so they are 3x each
    long_side1 = 3 * x
    long_side2 = 3 * x

    # The total length of the fence is the sum of all four sides
    total_length = x + x + long_side1 + long_side2

    # We know that the total length of the fence is 640 feet, so we can solve for x
    x = (640 - long_side1 - long_side2) / 2

    # The rusted side is one of the short sides, so we need to replace x feet of fence
    result = x
    return result

print(solution())