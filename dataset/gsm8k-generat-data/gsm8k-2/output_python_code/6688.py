def solution():
    """Mark donates soup to the 6 homeless shelters. Each one services 30 people and he decides to buy 10 cans of soup per person. How many cans of soup does Mark donate?"""
    num_shelters = 6
    num_people_per_shelter = 30
    num_cans_per_person = 10
    total_cans_of_soup = num_shelters * num_people_per_shelter * num_cans_per_person
    result = total_cans_of_soup
    return result

print(solution())