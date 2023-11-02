def solution():
    # Determine how many friends Ashley invited
    invited_friends = 20

    # Determine how many people each friend invited
    each_invited_one = 1

    # Determine how many friends showed up to the party with an additional person
    showed_up_with_one_more = invited_friends / 2

    # Determine the total number of people at the party, including Ashley
    total_people = invited_friends + invited_friends * each_invited_one + showed_up_with_one_more

    result = total_people
    return result

print(solution())