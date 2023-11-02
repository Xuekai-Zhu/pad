def solution():
    total_vaccinated = 650  # The clinic administered the vaccine to 650 people
    adults_percentage = 80  # 80% of the people vaccinated were adults

    # Calculate the number of adults vaccinated
    adults_vaccinated = (adults_percentage/100) * total_vaccinated

    # Calculate the number of children vaccinated
    children_vaccinated = total_vaccinated - adults_vaccinated
    result = children_vaccinated
    return result

print(solution())