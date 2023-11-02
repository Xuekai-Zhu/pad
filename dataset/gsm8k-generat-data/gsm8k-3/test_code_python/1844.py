def solution():
    """Miggy's mom brought home 3 bags of birthday hats. Each bag has 15 hats. Miggy accidentally tore off 5 hats. During the party, only 25 hats were used. How many hats were unused?"""
    # Define the number of bags and hats per bag
    num_bags = 3
    hats_per_bag = 15

    # Calculate the total number of hats
    total_hats = num_bags * hats_per_bag

    # Subtract the number of torn hats and used hats from the total hats
    unused_hats = total_hats - 5 - 25

    # Display the number of unused hats
    result = unused_hats
    return result

print(solution())