def solution():
    """It takes Nissa 10 seconds to clip each of her cats' nails. 90 seconds to clean each of her ears, and 5 minutes to shampoo her. If the cat has four claws on each foot, how many seconds does grooming her cat take total?"""
    # Define the time it takes to clip one claw and the number of claws
    CLIP_TIME = 10
    NUM_CLAWS = 4

    # Define the time it takes to clean one ear
    EAR_CLEAN_TIME = 90

    # Define the time it takes to shampoo
    SHAMPOO_TIME = 5 * 60

    # Calculate the total time to groom one cat
    time_per_cat = CLIP_TIME * NUM_CLAWS + EAR_CLEAN_TIME + SHAMPOO_TIME

    # Display the total time
    result = time_per_cat
    return result

print(solution())