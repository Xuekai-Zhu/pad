def solution():
    """Mark donates soup to the 6 homeless shelters. Each one services 30 people and he decides to buy 10 cans of soup per person. How many cans of soup does Mark donate?"""
    shelters = 6
    people_per_shelter = 30
    cans_per_person = 10
    total_cans = shelters * people_per_shelter * cans_per_person
    result = total_cans
    return result

print(solution())