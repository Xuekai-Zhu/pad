def solution():
    """Peter needs to buy birdseed to last a week. He knows that each parakeet eats 2 grams a day. His parrots eat 14 grams a day. His finches eat half of what a parakeet eats. If he has 3 parakeets, 2 parrots and 4 finches, how many grams of birdseed does he need to buy?"""
    # Define the number of birds
    parakeets = 3
    parrots = 2
    finches = 4

    # Define the amount of birdseed each type of bird eats per day
    parakeet_seed = 2
    parrot_seed = 14
    finch_seed = parakeet_seed / 2

    # Calculate the total amount of birdseed needed for a week
    total_seed = (parakeets * parakeet_seed + parrots * parrot_seed + finches * finch_seed) * 7

    result = total_seed
    return result

print(solution())