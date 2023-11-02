def solution():
    
    total_population = 80000
    gordonia_population = total_population / 2
    toadon_population = 0.6 * gordonia_population
    lake_bright_population = total_population - gordonia_population - toadon_population
    result = lake_bright_population
    return result

print(solution())