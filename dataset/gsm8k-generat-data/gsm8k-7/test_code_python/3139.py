def solution():
    num_white_beads = 51
    num_black_beads = 90

    # Calculate the number of black beads Charley pulls out
    num_pulled_black = num_black_beads / 6

    # Calculate the number of white beads Charley pulls out
    num_pulled_white = num_white_beads / 3

    # Calculate the total number of beads Charley pulls out
    total_pulled = num_pulled_black + num_pulled_white
    result = total_pulled
    return result

print(solution())