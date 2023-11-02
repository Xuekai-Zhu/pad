def solution():
    # Define the number of friends Roger shared with
    num_friends = 3

    # Calculate the total number of cans split among Roger and his friends
    total_cans = (num_friends + 1) * 2 + 2

    # Calculate the number of cans Michelle had to start with
    initial_cans = total_cans + 2

    result = initial_cans
    return result

print(solution())