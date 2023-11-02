def solution():
    """James dumps his whole collection of 500 Legos on the floor and starts building a castle out of them. He uses half the pieces before finishing and is told to put the rest away. He puts all of the leftover pieces back in the box they came from, except for 5 missing pieces that he can't find. How many Legos are in the box at the end?"""
    starting_legos = 500
    used_legos = starting_legos / 2
    leftover_legos = starting_legos - used_legos - 5
    result = leftover_legos
    return result

print(solution())