def solution():
    # Define the initial number of friends
    initial_friends = 100

    # Calculate the number of friends Mark keeps
    kept_friends = round(initial_friends * 0.4)

    # Calculate the number of friends Mark contacts
    contacted_friends = initial_friends - kept_friends

    # Calculate the number of friends who respond
    responding_friends = round(contacted_friends * 0.5)

    # Calculate the number of friends Mark has left after removing those who did not respond
    remaining_friends = kept_friends + responding_friends

    result = remaining_friends
    return result

print(solution())