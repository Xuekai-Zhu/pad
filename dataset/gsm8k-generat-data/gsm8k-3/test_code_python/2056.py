def solution():
    """Randy walks his dog twice a day.  After each walk, he wipes his dog's paws off with a baby wipe.  The baby wipes come 120 wipes per pack.  How many packs will he need to make sure he has enough wipes for 360 days?"""
    # Calculate the number of wipes used per day
    wipes_per_day = 2

    # Calculate the number of wipes used in 360 days
    wipes_in_360_days = wipes_per_day * 360

    # Calculate the number of packs of wipes needed
    packs_needed = (wipes_in_360_days // 120) + 1

    # Display the number of packs needed
    result = packs_needed
    return result

print(solution())