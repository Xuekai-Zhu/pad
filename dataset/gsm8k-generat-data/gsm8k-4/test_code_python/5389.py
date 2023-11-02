def solution():
    """It takes Nissa 10 seconds to clip each of her cats' nails. 90 seconds to clean each of her ears, and 5 minutes to shampoo her. If the cat has four claws on each foot, how many seconds does grooming her cat take total?"""
    # Define the time it takes to clip one nail and the number of nails per cat
    nail_time = 10
    nails_per_cat = 4 * 4  # four claws on each foot

    # Calculate the total time to clip nails for one cat
    nail_time_total = nail_time * nails_per_cat

    # Define the time it takes to clean one ear
    ear_time = 90

    # Calculate the total time to clean ears for one cat
    ear_time_total = ear_time * 2  # assuming two ears per cat

    # Define the time it takes to shampoo one cat
    shampoo_time = 5 * 60

    # Calculate the total grooming time for one cat
    total_time = nail_time_total + ear_time_total + shampoo_time

    result = total_time
    return result

print(solution())