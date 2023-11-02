def solution():
    # Define the amount of birdseed each type of bird eats per day
    parakeet_seed = 2
    parrot_seed = 14
    finch_seed = parakeet_seed / 2

    # Define the number of each type of bird
    num_parakeets = 3
    num_parrots = 2
    num_finches = 4

    # Calculate the total amount of birdseed needed for a day
    total_seed_per_day = (parakeet_seed * num_parakeets) + (parrot_seed * num_parrots) + (finch_seed * num_finches)

    # Calculate the total amount of birdseed needed for a week
    total_seed_per_week = total_seed_per_day * 7
    
    result = total_seed_per_week
    return result

print(solution())