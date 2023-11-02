def solution():
    # Find the total cost spent on the 7 pieces of clothing
    total_cost = 610

    # Find the cost of the two known pieces of clothing
    piece1_cost = 49
    piece2_cost = 81

    # Find the total cost of the remaining 5 pieces of clothing
    remaining_cost = total_cost - piece1_cost - piece2_cost

    # Find the cost of each of the remaining 5 pieces of clothing
    cost_per_piece = remaining_cost / 5

    result = cost_per_piece
    return result

print(solution())