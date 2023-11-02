def solution():
    """After being contracted to build 4000 bollards on each side of a road, a company was only able to install 3/4 of the total number of bollards required on all sides of the road. How many more bollards are they required to install on all sides of the remaining part of the road?"""
    # Define the total number of bollards required
    total_bollards = 4000 * 2

    # Calculate the number of bollards installed
    installed_bollards = total_bollards * 0.75

    # Calculate the number of bollards still required
    remaining_bollards = total_bollards - installed_bollards

    # Display the number of bollards still required
    result = remaining_bollards
    return result

print(solution())