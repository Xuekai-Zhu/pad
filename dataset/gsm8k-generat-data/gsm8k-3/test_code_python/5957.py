def solution():
    """Kendra tracks the different species of birds they spot on their birdwatching trip. On Monday they visited 5 sites and saw an average of 7 birds at each site. On Tuesday, Kendra visited 5 sites and saw an average of 5 birds at each site. On Wednesday visited 10 sites and saw an average of 8 birds at each site. On average, how many different birds did Kendra see on each site?"""
    # Calculate the total number of birds seen on Monday
    monday_birds = 5 * 7

    # Calculate the total number of birds seen on Tuesday
    tuesday_birds = 5 * 5

    # Calculate the total number of birds seen on Wednesday
    wednesday_birds = 10 * 8

    # Calculate the total number of birds seen on the entire trip
    total_birds = monday_birds + tuesday_birds + wednesday_birds

    # Calculate the average number of birds seen per site
    avg_birds_per_site = total_birds / 20

    # Display the result
    result = avg_birds_per_site
    return result

print(solution())