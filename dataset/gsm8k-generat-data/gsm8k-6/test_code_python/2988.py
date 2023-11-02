def solution():
    # Calculate the time Hadassah took to paint 1 painting
    time_per_painting = 6/12  # 6 hours to paint 12 paintings

    # Calculate the total time taken to paint 20 more paintings
    time_for_20_paintings = time_per_painting * 20

    # Calculate the total time taken to finish all the paintings
    total_time = 6 + time_for_20_paintings

    result = total_time
    return result

print(solution())