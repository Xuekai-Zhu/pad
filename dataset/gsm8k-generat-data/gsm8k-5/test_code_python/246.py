def solution():
    # Set up the problem as a system of equations
    # Let x be the number of boys in the family
    # Then, the number of girls in the family is 180 - x
    # Also, the ratio of boys to girls is 5:7, so we have:
    # 5x / 7(180 - x) = 1  (since the total number of children is 180)
    # Solving for x, we get:
    x = 75  # There are 75 boys in the family

    # Calculate how much money each boy receives
    amount_per_boy = 3900 / 75
    result = amount_per_boy
    return result

print(solution())