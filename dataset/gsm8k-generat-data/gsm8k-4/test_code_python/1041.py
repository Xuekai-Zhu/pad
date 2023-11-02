def solution():
    """A clinic administered the covid vaccine to 650 people. 80% of the people were adults. How many of the vaccinated people were children?"""
    # Define the total number of vaccinated people
    total_vaccinated = 650

    # Calculate the number of adults vaccinated
    adult_vaccinated = total_vaccinated * 0.8

    # Calculate the number of children vaccinated
    children_vaccinated = total_vaccinated - adult_vaccinated

    # return the result
    result = children_vaccinated
    return result

print(solution())