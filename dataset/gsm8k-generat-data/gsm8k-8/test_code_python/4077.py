def solution():
    # Calculate Gordonia's population
    gordonia_population = 80000 / 2

    # Calculate Toadon's population
    toadon_population = 0.6 * gordonia_population

    # Calculate Lake Bright's population
    lake_bright_population = 80000 - gordonia_population - toadon_population
    result = lake_bright_population
    return result

print(solution())