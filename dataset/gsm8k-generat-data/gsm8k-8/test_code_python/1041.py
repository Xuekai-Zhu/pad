def solution():
    # Calculate the number of adult vaccinated people
    adult_vaccinated = 0.8 * 650
    
    # Calculate the number of children vaccinated
    children_vaccinated = 650 - adult_vaccinated
    
    result = children_vaccinated
    return result

print(solution())