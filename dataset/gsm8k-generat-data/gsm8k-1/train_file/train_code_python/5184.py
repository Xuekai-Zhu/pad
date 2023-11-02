def solution():
    """Shelly and Sam love to go deep sea fishing for swordfish. Each time they go deep sea fishing, Shelly catches 2 less than five swordfish, and Sam catches one less swordfish than Shelly. If Sam and Shelly go fishing 5 times, how many swordfish do they catch in total?"""
    swordfish_shelly = 0
    swordfish_sam = 0
    for i in range(5):
        swordfish_shelly += (5 - 2) - 2
        swordfish_sam += (5 - 2) - 3
    total_swordfish = swordfish_shelly + swordfish_sam
    result = total_swordfish
    return result

print(solution())