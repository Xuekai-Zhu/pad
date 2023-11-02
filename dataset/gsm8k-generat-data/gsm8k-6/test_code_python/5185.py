def solution():
    total_swordfish = 0
    for i in range(5):
        shelly_catches = 5 - 2 - i*2  # Shelly catches 2 less than five swordfish
        sam_catches = shelly_catches - 1  # Sam catches one less swordfish than Shelly
        total_catches = shelly_catches + sam_catches
        total_swordfish += total_catches

    result = total_swordfish
    return result

print(solution())