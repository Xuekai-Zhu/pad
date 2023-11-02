def solution():
    # Calculate the total number of birds spotted by Kendra
    total_birds = 5 * 7 + 5 * 5 + 10 * 8  # Kendra visited 5 sites on Monday and Tuesday, and 10 sites on Wednesday
    total_sites = 5 + 5 + 10  # Kendra visited 5 sites on Monday and Tuesday, and 10 sites on Wednesday
    birds_per_site = total_birds / total_sites  # Calculate the average number of birds spotted per site

    result = birds_per_site
    return result

print(solution())