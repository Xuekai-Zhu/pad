def solution():
    """While camping, Cyrus counted 14 mosquito bites on his arms and legs. He later counted another 10 on his body. While he was suffering, his entire family of 6 other people only got a total of half the number of bites that Cyrus got. If they all have an equal number of bites, how many mosquito bites does each member of the rest of Cyrus' family have?"""
    total_bites = 14 + 10
    family_bites = total_bites / 2
    num_family_members = 6
    bites_per_family_member = family_bites / num_family_members
    result = bites_per_family_member
    return result

print(solution())