def solution():
    """It takes Nissa 10 seconds to clip each of her cats' nails. 90 seconds to clean each of her ears, and 5 minutes to shampoo her.
    If the cat has four claws on each foot, how many seconds does grooming her cat take total?"""
    nails_per_foot = 4
    time_per_nail = 10
    ears_cleaning_time = 90
    shampoo_time = 5 * 60
    total_nail_time = time_per_nail * nails_per_foot
    total_grooming_time = total_nail_time + ears_cleaning_time + shampoo_time
    result = total_grooming_time
    return result

print(solution())