def solution():
    """Charley has a bag that contains 51 white beads and 90 black beads. He reaches in the bag and pulls out 1/6 of the black beads and a third of the white beads. How many beads in total did Charley pull out?"""
    white_beads = 51
    black_beads = 90
    black_pulled = black_beads / 6
    white_pulled = white_beads / 3
    total_pulled = black_pulled + white_pulled
    result = total_pulled
    return result

print(solution())