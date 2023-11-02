def solution():
    # Calculate the total number of birds seen on Monday
    birds_on_monday = 5 * 7

    # Calculate the total number of birds seen on Tuesday
    birds_on_tuesday = 5 * 5

    # Calculate the total number of birds seen on Wednesday
    birds_on_wednesday = 10 * 8

    # Calculate the total number of birds seen over three days
    total_birds_seen = birds_on_monday + birds_on_tuesday + birds_on_wednesday

    # Calculate the average number of birds seen per site
    average_birds_per_site = total_birds_seen / 20  # Kendra visited a total of 20 sites

    result = average_birds_per_site
    return result

print(solution())