def solution():
    
    total_population = 5000
    male_population = 2000
    female_population = total_population - male_population
    females_with_glasses = int(0.3 * female_population)
    result = females_with_glasses
    return result

print(solution())