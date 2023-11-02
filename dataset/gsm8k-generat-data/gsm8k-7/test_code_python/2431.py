def solution():
    total_pencils = 50

    # Let x be the number of pencils Sabrina has
    # Then Justin has 8 more than twice as many pencils as Sabrina
    # So Justin has 2x + 8 pencils
    # And the total number of pencils is x + (2x + 8) = 3x + 8
    # We know the total number of pencils is 50, so we can solve for x

    x = (total_pencils - 8) / 3

    # Sabrina has x pencils
    result = x
    return result

print(solution())