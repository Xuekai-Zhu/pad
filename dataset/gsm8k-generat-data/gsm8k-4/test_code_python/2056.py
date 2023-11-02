def solution():
    """Randy walks his dog twice a day. After each walk, he wipes his dog's paws off with a baby wipe. The baby wipes come 120 wipes per pack. How many packs will he need to make sure he has enough wipes for 360 days?"""
    # Define the number of dog walks per day
    walks_per_day = 2

    # Define the number of days
    days = 360

    # Calculate the total number of dog walks
    total_walks = walks_per_day * days

    # Calculate the total number of baby wipes needed
    total_wipes = total_walks

    # Calculate the number of packs needed
    packs_needed = total_wipes / 120

    # Round up to the nearest whole pack
    packs_needed = math.ceil(packs_needed)

    result = packs_needed
    return result

print(solution())