def solution():
    """James dumps his whole collection of 500 Legos on the floor and starts building a castle out of them.  He uses half the pieces before finishing and is told to put the rest away.  He puts all of the leftover pieces back in the box they came from, except for 5 missing pieces that he can't find.  How many Legos are in the box at the end?"""
    # Define the initial number of Legos
    initial_legos = 500

    # Calculate the number of Legos used in the castle
    castle_legos = initial_legos / 2

    # Calculate the number of Legos left in the box
    left_legos = initial_legos - castle_legos - 5

    # return the result
    result = left_legos
    return result

print(solution())