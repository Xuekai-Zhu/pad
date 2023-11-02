def solution():
    
    total_population = 5000
    male_population = 2000
    female_population = total_population - male_population
    percentage_wearing_glasses = 30
    females_wearing_glasses = (percentage_wearing_glasses / 100) * female_population
    
    return females_wearing_glasses

print(solution())