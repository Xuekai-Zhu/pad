def solution():
    # Calculate the time to clip all of the cat's nails
    time_to_clip = 10 * (4*4)  # Nissa has to clip each of the cat's 16 nails, which takes her 10 seconds per nail

    # Calculate the time to clean both of the cat's ears
    time_to_clean_ears = 90 * 2  # Nissa has to clean both of the cat's ears, which takes her 90 seconds per ear

    # Calculate the time to shampoo the cat
    time_to_shampoo = 5 * 60  # Nissa has to shampoo the cat, which takes her 5 minutes or 300 seconds

    # Calculate the total time to groom the cat
    total_time = time_to_clip + time_to_clean_ears + time_to_shampoo
    result = total_time
    return result

print(solution())