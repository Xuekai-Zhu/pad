def solution():
    """A clinic administered the covid vaccine to 650 people. 80% of the people were adults. How many of the vaccinated people were children?"""
    total_vaccinated = 650
    adult_percent = 80
    adult_vaccinated = total_vaccinated * (adult_percent / 100)
    children_vaccinated = total_vaccinated - adult_vaccinated
    result = children_vaccinated
    return result

print(solution())