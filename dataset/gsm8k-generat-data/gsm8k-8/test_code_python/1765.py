def solution():
    # Calculate the total number of worms needed for 6 babies for 1 day
    worms_per_day = 6 * 3

    # Calculate the total number of worms needed for 6 babies for 3 days
    total_worms_needed = 3 * worms_per_day

    # Calculate the total number of worms Mama bird has
    total_worms_available = 9 + 13 - 2

    # Calculate the number of worms Mama bird still needs to catch
    worms_needed = total_worms_needed - total_worms_available

    result = worms_needed
    return result

print(solution())