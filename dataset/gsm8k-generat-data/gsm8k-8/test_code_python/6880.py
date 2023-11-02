def solution():
    # Calculate the total number of mosquito bites Cyrus got
    total_cyrus_bites = 14 + 10

    # Calculate the total number of bites the rest of his family got
    family_bites = total_cyrus_bites / 2

    # Calculate the number of bites per family member (including Cyrus)
    total_family_members = 7
    bites_per_member = (total_cyrus_bites + family_bites) / total_family_members

    result = bites_per_member
    return result

print(solution())