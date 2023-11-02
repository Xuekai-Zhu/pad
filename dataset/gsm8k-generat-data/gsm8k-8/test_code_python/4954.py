def solution():
    # Calculate the total cost of the 7 pieces of clothing
    total_cost = 610

    # Determine the cost of the two known pieces of clothing
    known_cost = 49 + 81

    # Calculate the cost of the remaining 5 pieces of clothing
    remaining_cost = total_cost - known_cost

    # Calculate the cost of one of the remaining pieces of clothing
    one_piece_cost = remaining_cost / 5
    result = one_piece_cost
    return result

print(solution())