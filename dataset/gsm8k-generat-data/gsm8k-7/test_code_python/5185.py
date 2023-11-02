def solution():
    num_fishing_trips = 5

    total_swordfish = 0
    for i in range(num_fishing_trips):
        shelly_swordfish = (5 - 2)  # Shelly catches 2 less than five swordfish
        sam_swordfish = (shelly_swordfish - 1)  # Sam catches one less swordfish than Shelly
        total_swordfish += (shelly_swordfish + sam_swordfish)

    result = total_swordfish
    return result

print(solution())