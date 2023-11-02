def solution():
    # Define the number of bags and hats per bag
    num_bags = 3
    hats_per_bag = 15

    # Calculate the total number of hats before tearing
    total_hats = num_bags * hats_per_bag

    # Subtract the torn hats and used hats to get the number of unused hats
    unused_hats = total_hats - 5 - 25
    result = unused_hats
    return result

print(solution())