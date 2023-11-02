def solution():
    monday_sites = 5
    monday_avg_birds = 7
    tuesday_sites = 5
    tuesday_avg_birds = 5
    wednesday_sites = 10
    wednesday_avg_birds = 8

    # Calculate the total number of birds seen on Monday
    monday_total_birds = monday_sites * monday_avg_birds

    # Calculate the total number of birds seen on Tuesday
    tuesday_total_birds = tuesday_sites * tuesday_avg_birds

    # Calculate the total number of birds seen on Wednesday
    wednesday_total_birds = wednesday_sites * wednesday_avg_birds

    # Calculate the total number of sites visited
    total_sites = monday_sites + tuesday_sites + wednesday_sites

    # Calculate the total number of birds seen
    total_birds = monday_total_birds + tuesday_total_birds + wednesday_total_birds

    # Calculate the average number of birds seen per site
    avg_birds_per_site = total_birds / total_sites
    result = avg_birds_per_site
    return result

print(solution())