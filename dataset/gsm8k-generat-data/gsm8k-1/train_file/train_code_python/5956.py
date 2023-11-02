def solution():
    """Kendra tracks the different species of birds they spot on their birdwatching trip. On Monday they visited 5 sites and saw an average of 7 birds at each site. On Tuesday, Kendra visited 5 sites and saw an average of 5 birds at each site. On Wednesday visited 10 sites and saw an average of 8 birds at each site. On average, how many different birds did Kendra see on each site?"""
    total_sites = 20
    total_birds = (5*7) + (5*5) + (10*8)
    average_birds_per_site = total_birds / total_sites
    result = average_birds_per_site
    return result

print(solution())