def solution():
    # Define the number of pieces in each puzzle
    puzzle1 = 1000
    puzzle2 = puzzle3 = puzzle1 * 1.5

    # Calculate the total number of pieces
    total_pieces = puzzle1 + puzzle2 + puzzle3
    result = total_pieces
    return result

print(solution())