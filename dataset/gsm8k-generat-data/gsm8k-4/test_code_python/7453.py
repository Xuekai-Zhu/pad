def solution():
    """James and John combine their friends lists. James has 75 friends. John has 3 times as many friends as James. They share 25 friends. How many people are on the combined list?"""
    # Define the number of friends James has
    james_friends = 75

    # Define the number of friends John has
    john_friends = james_friends * 3

    # Define the number of friends they share
    shared_friends = 25

    # Calculate the total number of friends on the combined list
    total_friends = james_friends + john_friends - shared_friends

    # Return the result
    result = total_friends
    return result

print(solution())