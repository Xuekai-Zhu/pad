def solution():
    """While camping, Cyrus counted 14 mosquito bites on his arms and legs. He later counted another 10 on his body. While he was suffering, his entire family of 6 other people only got a total of half the number of bites that Cyrus got. If they all have an equal number of bites, how many mosquito bites does each member of the rest of Cyrus' family have?"""
    cyrus_bites = 14 + 10
    total_family_bites = cyrus_bites * 2
    per_family_member_bites = total_family_bites / 6
    result = per_family_member_bites
    return result

print(solution())