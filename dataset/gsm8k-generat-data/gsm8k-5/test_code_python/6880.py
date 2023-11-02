def solution():
    # Total mosquito bites Cyrus got
    total_cyrus_bites = 14 + 10

    # Total mosquito bites the rest of the family got
    total_family_bites = total_cyrus_bites / 2

    # Total number of people in the family
    num_family_members = 6

    # Calculate the average number of bites per family member
    avg_bites_per_person = total_family_bites / num_family_members
    result = avg_bites_per_person
    return result

print(solution())