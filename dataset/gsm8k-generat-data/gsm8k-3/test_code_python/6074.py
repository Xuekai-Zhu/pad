def solution():
    """James dumps his whole collection of 500 Legos on the floor and starts building a castle out of them.  He uses half the pieces before finishing and is told to put the rest away.  He puts all of the leftover pieces back in the box they came from, except for 5 missing pieces that he can't find.  How many Legos are in the box at the end?"""
    # Define the number of Legos James started with
    starting_legos = 500

    # Calculate the number of Legos used to build the castle
    castle_legos = starting_legos / 2

    # Calculate the number of Legos left in the box
    box_legos = starting_legos - castle_legos - 5

    # Display the number of Legos left in the box
    result = box_legos
    return result

print(solution())