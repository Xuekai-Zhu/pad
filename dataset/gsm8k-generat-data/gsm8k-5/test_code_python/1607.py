def solution():
    # Let's assume Jane has x dollars
    x = 1

    # Then Jean has 3 times as much money as Jane
    j = 3 * x

    # The total amount of money they have is $76
    total = 76

    # So we have the equation j + x = total
    # We can substitute j with 3x to get the equation 4x = total
    # Solving for x gives us x = total/4
    x = total/4

    # Now that we know x, we can find the amount of money Jean has
    j = 3 * x

    result = j
    return result

print(solution())