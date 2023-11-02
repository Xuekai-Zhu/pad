def solution():
    """While camping, Cyrus counted 14 mosquito bites on his arms and legs. He later counted another 10 on his body. While he was suffering, his entire family of 6 other people only got a total of half the number of bites that Cyrus got. If they all have an equal number of bites, how many mosquito bites does each member of the rest of Cyrus' family have?"""
    # Calculate the total number of mosquito bites Cyrus got
    cyrus_bites = 14 + 10

    # Calculate the total number of bites for the rest of Cyrus' family
    family_bites = cyrus_bites / 2

    # Calculate the number of family members
    family_members = 6

    # Calculate the number of bites per family member
    bites_per_member = family_bites / family_members

    result = bites_per_member
    return result

print(solution())