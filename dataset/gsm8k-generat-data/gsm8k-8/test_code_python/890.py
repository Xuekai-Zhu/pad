def solution():
    # Let's represent the second throw distance as x
    x = 0

    # The first throw is then twice that distance
    first_throw = 2 * x

    # The third throw is twice the distance of the first throw
    third_throw = 2 * first_throw

    # We know the sum of all three throws is 1050
    # So we can solve for x and then find the distance of the first throw
    x = (1050 / 5) / 3
    first_throw = 2 * x
    result = first_throw
    return result

print(solution())