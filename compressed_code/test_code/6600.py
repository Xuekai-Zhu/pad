def solution():
    
    total_vaccinated = 650
    adult_percent = 80
    adult_vaccinated = total_vaccinated * (adult_percent / 100)
    children_vaccinated = total_vaccinated - adult_vaccinated
    result = children_vaccinated
    return result

print(solution())