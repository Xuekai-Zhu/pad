def solution():
    total_oranges = 180

    # Let x be the number of oranges sold by Emily
    # Then, Alice sold 2x oranges
    x = total_oranges / 3   # Total oranges divided by 3 since Alice sold twice as many

    alice_oranges = 2 * x
    result = alice_oranges
    return result

print(solution())