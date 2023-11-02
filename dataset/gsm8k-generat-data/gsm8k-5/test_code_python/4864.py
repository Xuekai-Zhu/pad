def solution():
    # Calculate the time it takes to knit one complete outfit
    time_per_outfit = 2 + 3 + 2 + 2 * 1.5 + 6  # Time to knit each item added up

    # Calculate the total time to knit outfits for all 3 grandchildren
    total_time = time_per_outfit * 3  # Three grandchildren

    result = total_time
    return result

print(solution())