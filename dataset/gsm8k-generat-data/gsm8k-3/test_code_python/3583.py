def solution():
    """Carson is covering the high school football field with grass seed. Each square meter needs three times as much seed as fertilizer. If Carson uses 60 gallons of seed and fertilizer combined, how many gallons of seed does he use?"""
    # Define the ratio of seed to fertilizer needed per square meter
    SEED_TO_FERTILIZER_RATIO = 3

    # Calculate the total amount of seed and fertilizer used per square meter
    total = 1 + SEED_TO_FERTILIZER_RATIO 

    # Calculate the fraction of the total that is seed
    seed_fraction = 1 / total

    # Calculate the total gallons of seed used for the football field
    total_seed = 60 * seed_fraction

    result = total_seed 
    return result

print(solution())