def solution():
    total_rolls = 12  # Chandler needs to sell 12 rolls of wrapping paper
    sold_rolls = 3 + 4 + 3  # Chandler has already sold 3 rolls to his grandmother, 4 rolls to his uncle, and 3 rolls to a neighbor
    remaining_rolls = total_rolls - sold_rolls  # Chandler needs to sell the remaining rolls

    result = remaining_rolls
    return result

print(solution())