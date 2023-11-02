def solution():
    bags_of_hats = 3  # Miggy's mom brought home 3 bags of hats
    hats_per_bag = 15  # Each bag has 15 hats
    hats_torn_off = 5  # Miggy accidentally tore off 5 hats
    hats_used = 25  # During the party, only 25 hats were used

    # Calculate the total number of hats
    total_hats = bags_of_hats * hats_per_bag

    # Calculate the number of unused hats
    unused_hats = total_hats - (hats_torn_off + hats_used)
    result = unused_hats
    return result

print(solution())