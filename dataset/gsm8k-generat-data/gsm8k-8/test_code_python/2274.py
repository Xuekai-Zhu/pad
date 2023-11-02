def solution():
    # Define the initial number of friends
    num_friends = 20

    # Subtract the two friends James got into an argument with
    num_friends -= 2

    # Add the new friend he made on his way back home
    num_friends += 1

    result = num_friends
    return result

print(solution())