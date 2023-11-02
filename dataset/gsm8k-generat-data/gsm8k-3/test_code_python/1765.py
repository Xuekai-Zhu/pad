def solution():
    """Mama bird has 6 babies in the nest.  She needs to feed each baby 3 worms a day.  Papa bird caught 9 worms. If she caught 13 worms and had 2 stolen, how many more does she need to catch to feed them for 3 days?"""
    # Define number of babies and worms needed per day
    NUM_BABIES = 6
    WORMS_PER_DAY = 3

    # Calculate total worms needed for 3 days
    total_worms = NUM_BABIES * WORMS_PER_DAY * 3

    # Calculate total worms already caught
    total_caught = 9 + 13 - 2

    # Calculate remaining worms needed
    remaining_worms = total_worms - total_caught

    # Display remaining worms needed
    result = remaining_worms
    return result

print(solution())