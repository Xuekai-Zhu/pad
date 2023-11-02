def solution():
    # Number of donuts Andrew asked for originally
    initial_donuts = 3

    # Number of friends Andrew originally planned for
    initial_friends = 2

    # Number of friends added later
    added_friends = 2

    # Total number of friends
    total_friends = initial_friends + added_friends

    # Total number of donuts needed (including extra donut for each friend)
    total_donuts = (initial_donuts * total_friends) + total_friends

    result = total_donuts
    return result

print(solution())