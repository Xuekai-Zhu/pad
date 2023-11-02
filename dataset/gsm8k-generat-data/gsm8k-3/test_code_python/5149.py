def solution():
    """Danny has a huge fish tank that contains 94 guppies, 76 angelfish, 89 tiger sharks, and 58 Oscar fish. If he sells 30 guppies, 48 angelfish, 17 tiger sharks, and 24 Oscar fish. How many fish will remain?"""
    # Define the initial number of each type of fish
    guppies = 94
    angelfish = 76
    tiger_sharks = 89
    oscar_fish = 58

    # Reduce the number of each type of fish by the number sold
    guppies -= 30
    angelfish -= 48
    tiger_sharks -= 17
    oscar_fish -= 24

    # Calculate the total number of fish remaining
    total_fish = guppies + angelfish + tiger_sharks + oscar_fish

    # Display the total number of fish remaining
    result = total_fish
    return result

print(solution())