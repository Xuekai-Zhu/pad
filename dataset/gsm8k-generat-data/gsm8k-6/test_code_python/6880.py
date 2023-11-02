def solution():
    # Calculate the total number of mosquito bites Cyrus got
    total_bites_cyrus = 14 + 10

    # Calculate the total number of mosquito bites Cyrus' family got
    total_bites_family = total_bites_cyrus / 2

    # Calculate the number of bites each member of Cyrus' family got
    bites_per_person = total_bites_family / 6
    result = bites_per_person
    return result

print(solution())