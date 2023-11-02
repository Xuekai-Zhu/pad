def solution():
    """James has 20 friends. Yesterday at work he got into an argument with 2 of his friends. Now he no longer considers them as friends. On his way back home, he made one more friend. So how many friends does James have left?"""
    # Define the initial number of friends
    initial_friends = 20

    # Define the number of friends James lost
    lost_friends = 2

    # Define the number of friends James gained
    gained_friends = 1

    # Calculate the number of friends James has left
    remaining_friends = initial_friends - lost_friends + gained_friends

    # Display the number of friends James has left
    result = remaining_friends
    return result

print(solution())