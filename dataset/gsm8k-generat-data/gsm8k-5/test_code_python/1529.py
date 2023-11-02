def solution():
    total_population = 5000
    male_population = 2000
    female_population = total_population - male_population

    # Calculate the number of females who wear glasses
    female_glasses_population = int(female_population * 0.3)

    result = female_glasses_population
    return result

print(solution())