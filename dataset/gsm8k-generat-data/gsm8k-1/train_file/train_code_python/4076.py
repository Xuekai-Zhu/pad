def solution():
    """Three towns, Toadon, Gordonia, and Lake Bright, have 80000 people. Gordonia has 1/2 times the total population in the three cities. If the population of Toadon is 60 percent of Gordonia's population, how many people live in Lake Bright?"""
    total_population = 80000
    gordonia_population = total_population / 2
    toadon_population = 0.6 * gordonia_population
    lake_bright_population = total_population - gordonia_population - toadon_population
    result = lake_bright_population
    return result

print(solution())