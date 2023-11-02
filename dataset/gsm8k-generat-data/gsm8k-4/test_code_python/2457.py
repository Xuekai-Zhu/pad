def solution():
    """A colony of bees can contain up to 80000 individuals. In winter they are more exposed to death, and if the winter is really cold the bees can begin to die slowly. If the colony starts to lose 1200 bees per day, how many days will pass until the number of bees in the colony reaches a fourth of its initial number?"""
    # Define the initial number of bees and the rate of bee loss per day
    INITIAL_BEES = 80000
    BEE_LOSS_PER_DAY = 1200

    # Calculate the number of days it will take for the colony to reach a fourth of its initial number of bees
    days = (INITIAL_BEES / 4 - BEE_LOSS_PER_DAY) / BEE_LOSS_PER_DAY

    # Round up to the nearest whole number of days
    days = int(round(days + 0.5))

    # Return the result
    result = days
    return result

print(solution())