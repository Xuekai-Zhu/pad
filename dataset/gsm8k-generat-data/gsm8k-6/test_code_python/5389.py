def solution():
    # Calculate the total time it takes to clip all of the cat's nails
    total_nail_time = 10 * 4  # 4 claws on each foot

    # Calculate the total time it takes to clean both ears
    total_ear_time = 90 * 2  # there are 2 ears to clean

    # Calculate the total time it takes to shampoo the cat
    total_shampoo_time = 5 * 60  # 5 minutes in seconds

    # Calculate the total grooming time
    total_grooming_time = total_nail_time + total_ear_time + total_shampoo_time
    result = total_grooming_time
    return result

print(solution())