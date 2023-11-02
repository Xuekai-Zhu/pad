def solution():
    # Calculate the total number of birds seen on Monday
    monday_birds = 5 * 7

    # Calculate the total number of birds seen on Tuesday
    tuesday_birds = 5 * 5

    # Calculate the total number of birds seen on Wednesday
    wednesday_birds = 10 * 8

    # Calculate the total number of birds seen over the three days
    total_birds = monday_birds + tuesday_birds + wednesday_birds

    # Calculate the average number of birds seen per site
    average_birds_per_site = total_birds / (5 + 5 + 10)
    result = average_birds_per_site
    return result

print(solution())