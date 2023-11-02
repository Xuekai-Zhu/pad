def solution():
    """A clinic administered the covid vaccine to 650 people. 80% of the people were adults. How many of the vaccinated people were children?"""
    total_people = 650
    adult_percentage = 0.8
    adult_count = total_people * adult_percentage
    child_count = total_people - adult_count
    result = child_count
    return result

print(solution())