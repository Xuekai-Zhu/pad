def solution():
    total_population = 80000  # The total population of the three towns is 80000
    gordonia_population = total_population/2  # Gordonia has 1/2 times the total population

    # Calculate the population of Toadon
    toadon_population = 0.6 * gordonia_population  

    # Calculate the population of Lake Bright
    lake_bright_population = total_population - (gordonia_population + toadon_population)
    result = lake_bright_population
    return result

print(solution())