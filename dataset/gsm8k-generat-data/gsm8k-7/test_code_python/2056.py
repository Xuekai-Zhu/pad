def solution():
    walks_per_day = 2
    wipes_per_walk = 1
    wipes_per_pack = 120
    num_days = 360

    # Calculate the total number of wipes used per day
    total_wipes_per_day = walks_per_day * wipes_per_walk

    # Calculate the total number of wipes used in 360 days
    total_wipes = total_wipes_per_day * num_days

    # Calculate the total number of packs needed to have enough wipes
    num_packs = total_wipes // wipes_per_pack + 1
    result = num_packs
    return result

print(solution())