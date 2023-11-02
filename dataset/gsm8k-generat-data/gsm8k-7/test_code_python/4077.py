def solution():
    total_population = 80000

    # Gordonia has 1/2 times the total population in the three cities
    gordonia_population = total_population / 2

    # Calculate the population of Toadon
    toadon_population = gordonia_population * 0.6

    # Calculate the population of Lake Bright by subtracting the population
    # of Gordonia and Toadon from the total population
    lake_bright_population = total_population - gordonia_population - toadon_population
    result = lake_bright_population
    return result

print(solution())