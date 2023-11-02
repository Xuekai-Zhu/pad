def solution():
    # Calculate the total number of baby wipes Randy needs for his dog per day
    wipes_per_day = 2

    # Calculate the total number of baby wipes Randy needs for his dog for 360 days
    total_wipes = wipes_per_day * 360

    # Calculate the number of packs Randy needs to buy
    wipes_per_pack = 120
    packs = total_wipes // wipes_per_pack  # use floor division to get the whole number of packs needed
    if total_wipes % wipes_per_pack != 0:  # if there are extra wipes left over, add one more pack
        packs += 1

    result = packs
    return result

print(solution())