def solution():
    # Calculate the number of adults vaccinated
    adults_vaccinated = 0.8 * 650

    # Calculate the number of children vaccinated
    children_vaccinated = 650 - adults_vaccinated
    result = children_vaccinated
    return result

print(solution())