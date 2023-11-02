def solution():
    """After being contracted to build 4000 bollards on each side of a road, a company was only able to install 3/4 of the total number
    of bollards required on all sides of the road. How many more bollards are they required to install on all sides of the remaining part of the road?"""
    total_bollards = 4000 * 2 # Two sides of the road
    installed_bollards = total_bollards * (3/4)
    remaining_bollards = total_bollards - installed_bollards
    result = remaining_bollards
    return result

print(solution())