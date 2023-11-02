def solution():
    total_population = 80000  # total population of the three towns
    gordonia_population = total_population / 2  # Gordonia has 1/2 times the total population
    toadon_population = 0.6 * gordonia_population  # Toadon's population is 60% of Gordonia's population
    lake_bright_population = total_population - gordonia_population - toadon_population  # population of Lake Bright is the difference between total population and the populations of Gordonia and Toadon
    result = lake_bright_population
    return result

print(solution())