def solution():
    """James and John combine their friends lists.  James has 75 friends.  John has 3 times as many friends as James.  They share 25 friends.  How many people are on the combined list?"""
    # Define the number of friends James has
    james_friends = 75

    # Calculate the number of friends John has
    john_friends = 3 * james_friends

    # Calculate the number of friends they share
    shared_friends = 25

    # Calculate the total number of unique friends
    total_friends = james_friends + john_friends - shared_friends

    # Display the total number of friends
    result = total_friends
    return result

print(solution())