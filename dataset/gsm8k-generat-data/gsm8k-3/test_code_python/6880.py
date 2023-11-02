def solution():
    """While camping, Cyrus counted 14 mosquito bites on his arms and legs. He later counted another 10 on his body. While he was suffering, his entire family of 6 other people only got a total of half the number of bites that Cyrus got. If they all have an equal number of bites, how many mosquito bites does each member of the rest of Cyrus' family have?"""
    # Calculate the total number of mosquito bites that Cyrus got
    cyrus_bites = 14 + 10

    # Calculate the total number of mosquito bites that Cyrus' family got
    family_bites = cyrus_bites / 2

    # Calculate the number of bites each member of Cyrus' family got
    family_members = 6
    member_bites = family_bites / family_members

    # Display the number of mosquito bites each member of Cyrus' family got
    result = member_bites
    return result

print(solution())