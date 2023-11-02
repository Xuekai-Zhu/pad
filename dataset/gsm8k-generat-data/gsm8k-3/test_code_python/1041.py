def solution():
    """A clinic administered the covid vaccine to 650 people. 80% of the people were adults. How many of the vaccinated people were children?"""
    # Define the total number of people vaccinated
    total_vaccinated = 650

    # Calculate the number of adults vaccinated
    adults_vaccinated = int(total_vaccinated * 0.8)

    # Calculate the number of children vaccinated
    children_vaccinated = total_vaccinated - adults_vaccinated

    # Display the number of children vaccinated
    result = children_vaccinated
    return result

print(solution())