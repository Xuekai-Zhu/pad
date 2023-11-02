def solution():
    """Mama bird has 6 babies in the nest. She needs to feed each baby 3 worms a day. Papa bird caught 9 worms. If she caught 13 worms and had 2 stolen, how many more does she need to catch to feed them for 3 days?"""
    # Define the number of babies and the number of worms each baby needs per day
    num_babies = 6
    worms_per_baby = 3

    # Calculate the total number of worms needed in a day
    total_worms_per_day = num_babies * worms_per_baby

    # Calculate the total number of worms available
    total_worms_available = 9 + 13 - 2

    # Calculate the total number of worms needed for 3 days
    total_worms_needed = total_worms_per_day * 3

    # Calculate the number of additional worms needed
    additional_worms_needed = total_worms_needed - total_worms_available

    # return the result
    result = additional_worms_needed
    return result

print(solution())