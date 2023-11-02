def solution():
    num_puzzles = 2
    num_pieces_per_puzzle = 2000
    pieces_per_minute = 10

    # Calculate the total number of pieces in both puzzles
    total_pieces = num_puzzles * num_pieces_per_puzzle

    # Calculate the total number of minutes to complete both puzzles
    total_minutes = (total_pieces / pieces_per_minute) / 100

    result = total_minutes
    return result

print(solution())