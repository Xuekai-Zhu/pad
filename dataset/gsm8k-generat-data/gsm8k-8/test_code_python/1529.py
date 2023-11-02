def solution():
    # Calculate the number of females in the town
    total_population = 5000
    males = 2000
    females = total_population - males

    # Calculate the number of females who wear glasses
    female_glasses_percentage = 30/100
    female_glasses = females * female_glasses_percentage

    result = female_glasses
    return result

print(solution())