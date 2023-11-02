def solution():
    # Calculate the original cost of the gift
    original_cost = 10 * x  # Let x be the original cost of the gift, before 4 friends dropped out

    # The remaining 6 friends split the original cost equally, plus $8 more per share
    new_cost_per_share = (original_cost / 6) + 8

    # Calculate the new total cost of the gift, after the cost per share increased by $8
    new_total_cost = new_cost_per_share * 6

    result = new_total_cost
    return result

print(solution())