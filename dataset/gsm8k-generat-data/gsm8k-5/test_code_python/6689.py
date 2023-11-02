def solution():
    shelters = 6  # Mark donates soup to 6 homeless shelters
    people_per_shelter = 30  # Each shelter services 30 people
    soup_per_person = 10  # Mark donates 10 cans of soup per person

    # Calculate the total number of cans of soup Mark donates
    total_cans_of_soup = shelters * people_per_shelter * soup_per_person
    result = total_cans_of_soup
    return result

print(solution())