def solution():
    num_reubens = 10
    num_pastramis = 5
    total_earnings = 55

    # Let x be the cost of a Reuben sandwich
    # Then the cost of a Pastrami sandwich is x + 2
    # We know that 10x + 5(x + 2) = 55
    # Simplifying, we get 15x + 10 = 55
    # Solving for x, we get x = 3

    # Therefore, the cost of a Pastrami sandwich is 3 + 2 = 5
    result = 5
    return result

print(solution())