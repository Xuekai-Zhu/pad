def solution():
    num_bags = 3
    hats_per_bag = 15
    hats_torn = 5
    hats_used = 25

    # Calculate the total number of hats that Miggy's mom brought home
    total_hats = num_bags * hats_per_bag

    # Calculate the total number of hats that were not torn
    hats_not_torn = total_hats - hats_torn

    # Calculate the number of unused hats
    unused_hats = hats_not_torn - hats_used
    result = unused_hats
    return result

print(solution())