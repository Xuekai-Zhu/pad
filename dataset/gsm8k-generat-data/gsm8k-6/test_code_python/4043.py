def solution():
    # Calculate the number of pieces in the second and third puzzles
    second_puzzle = 1000 * 1.5  # Second puzzle has 50% more pieces than the first one
    third_puzzle = 1000 * 1.5  # Third puzzle also has 50% more pieces than the first one

    # Calculate the total number of pieces in all three puzzles
    total_pieces = 1000 + second_puzzle + third_puzzle 
    result = total_pieces
    return result

print(solution())