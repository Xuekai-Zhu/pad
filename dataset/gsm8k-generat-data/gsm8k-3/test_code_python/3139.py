def solution():
    """Charley has a bag that contains 51 white beads and 90 black beads. He reaches in the bag and pulls out 1/6 of the black beads and a third of the white beads. How many beads in total did Charley pull out?"""
    # Define the initial number of white and black beads
    white_beads = 51
    black_beads = 90

    # Calculate the number of beads Charley pulled out
    black_pulled_out = black_beads / 6
    white_pulled_out = white_beads / 3

    # Calculate the total number of beads Charley pulled out
    total_pulled_out = black_pulled_out + white_pulled_out

    # Display the total number of beads Charley pulled out
    result = total_pulled_out
    return result

print(solution())