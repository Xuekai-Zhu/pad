def solution():
    white_beads = 51
    black_beads = 90

    # Calculate the number of black beads Charley pulls out
    black_pulled = black_beads / 6

    # Calculate the number of white beads Charley pulls out
    white_pulled = white_beads / 3

    # Calculate the total number of beads Charley pulls out
    total_pulled = black_pulled + white_pulled
    result = total_pulled
    return result

print(solution())