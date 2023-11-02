def solution():
    time_per_painting = 2  # Dawn takes 2 hours to paint 1 painting
    num_paintings = 12  # Dawn has to paint 12 paintings
    total_time = time_per_painting * num_paintings  # Calculate the total time Dawn will spend painting
    total_earnings = 3600  # Dawn will earn $3600 for the series of 12 paintings

    # Calculate Dawn's hourly rate
    hourly_rate = total_earnings / total_time
    result = hourly_rate
    return result

print(solution())