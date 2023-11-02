def solution():
    """Shelly and Sam love to go deep sea fishing for swordfish. Each time they go deep sea fishing, Shelly catches 2 less than five swordfish, and Sam catches one less swordfish than Shelly. If Sam and Shelly go fishing 5 times, how many swordfish do they catch in total?"""
    total_swordfish = 0
    for i in range(5):
        shelly_swordfish = 5 - 2 - i * 2
        sam_swordfish = shelly_swordfish - 1
        total_swordfish += shelly_swordfish + sam_swordfish

    result = total_swordfish
    return result

print(solution())