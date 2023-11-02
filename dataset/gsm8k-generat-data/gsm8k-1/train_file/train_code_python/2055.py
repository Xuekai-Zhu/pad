def solution():
    """Randy walks his dog twice a day. After each walk, he wipes his dog's paws off with a baby wipe. The baby wipes come 120 wipes per pack. How many packs will he need to make sure he has enough wipes for 360 days?"""
    walks_per_day = 2
    days = 360
    wipes_per_pack = 120
    total_wipes_needed = walks_per_day * days * wipes_per_day
    packs_needed = total_wipes_needed // wipes_per_pack + 1  # Adding one in case of remainder
    result = packs_needed
    return result

print(solution())