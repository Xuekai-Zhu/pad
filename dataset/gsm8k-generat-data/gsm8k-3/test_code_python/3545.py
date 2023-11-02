def solution():
    """Belle eats 4 dog biscuits and 2 rawhide bones every evening. If each rawhide bone is $1, and each dog biscuit is $0.25, then how much does it cost, in dollars, to feed Belle these treats for a week?"""
    # Define the cost of each treat
    BISCUIT_COST = 0.25
    BONE_COST = 1

    # Define the number of treats Belle eats each evening
    biscuits_per_evening = 4
    bones_per_evening = 2

    # Calculate the cost of Belle's treats each evening
    evening_cost = (biscuits_per_evening * BISCUIT_COST) + (bones_per_evening * BONE_COST)

    # Calculate the cost of Belle's treats for a week
    week_cost = evening_cost * 7

    # Display the cost of Belle's treats for a week
    result = week_cost
    return result

print(solution())