def solution():
    """Blanche found 12 pieces of green and 3 pieces of red sea glass. Rose found 9 pieces of red and 11 pieces of blue sea glass.
    If Dorothy found twice as many pieces of red glass as Blanche and Rose and three times as much blue sea glass as Rose,
    how many pieces did Dorothy have?"""
    # Calculate the total number of red and blue sea glass found by Blanche and Rose
    total_red = 3 + 9
    total_blue = 11

    # Calculate the number of red and blue sea glass found by Dorothy
    dorothy_red = 2 * total_red
    dorothy_blue = 3 * total_blue

    # Calculate the total number of sea glass pieces found by Dorothy
    total_dorothy = dorothy_red + dorothy_blue

    result = total_dorothy
    return result

print(solution())