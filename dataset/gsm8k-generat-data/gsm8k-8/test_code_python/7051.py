def solution():
    # Calculate the total number of bowls needed
    total_bowls = 800 * 0.15

    # Calculate the total number of minnows needed for the prizes
    total_minnows = total_bowls * 3

    # Calculate the number of minnows left over
    minnows_leftover = 600 - total_minnows
    result = minnows_leftover
    return result

print(solution())