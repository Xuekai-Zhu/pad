def solution():
    total_spent = 610  # Jangshe spent $610 in total
    expensive_piece = 81  # One piece cost $81
    cheaper_piece = 49  # Another piece cost $49
    num_other_pieces = 7 - 2  # There were 7 pieces of clothing in total, minus the 2 we already know the prices of
    total_other_pieces = total_spent - expensive_piece - cheaper_piece  # Total cost of the other pieces

    # Calculate the cost of one of the other pieces
    cost_one_piece = total_other_pieces / num_other_pieces
    result = cost_one_piece
    return result

print(solution())