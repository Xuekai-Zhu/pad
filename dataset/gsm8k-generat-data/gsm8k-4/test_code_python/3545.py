def solution():
    """Belle eats 4 dog biscuits and 2 rawhide bones every evening. If each rawhide bone is $1, and each dog biscuit is $0.25, then how much does it cost, in dollars, to feed Belle these treats for a week?"""
    # Define the cost of each dog biscuit and rawhide bone
    DOG_BISCUIT_COST = 0.25
    RAWHIDE_BONE_COST = 1

    # Calculate the cost of Belle's treats for one evening
    evening_cost = (4 * DOG_BISCUIT_COST) + (2 * RAWHIDE_BONE_COST)

    # Calculate the cost of Belle's treats for a week
    week_cost = evening_cost * 7

    # Return the final result
    result = week_cost
    return result

print(solution())