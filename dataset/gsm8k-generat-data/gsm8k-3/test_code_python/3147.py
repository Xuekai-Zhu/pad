def solution():
    """Peter needs to buy birdseed to last a week. He knows that each parakeet eats 2 grams a day. His parrots eat 14 grams a day. His finches eat half of what a parakeet eats. If he has 3 parakeets, 2 parrots, and 4 finches, how many grams of birdseed does he need to buy?"""
    # Define the amount of birdseed each type of bird eats per day
    PARAKEET_SEEDS = 2
    PARROT_SEEDS = 14
    FINCH_SEEDS = PARAKEET_SEEDS / 2

    # Define the number of each type of bird
    num_parakeets = 3
    num_parrots = 2
    num_finches = 4

    # Calculate the total amount of birdseed needed per day
    total_seed_per_day = (PARAKEET_SEEDS * num_parakeets) + (PARROT_SEEDS * num_parrots) + (FINCH_SEEDS * num_finches)

    # Calculate the total amount of birdseed needed for a week (7 days)
    total_seed_per_week = total_seed_per_day * 7

    # Display the total amount of birdseed needed
    result = total_seed_per_week
    return result

print(solution())