def solution():
    """James has 20 friends. Yesterday at work he got into an argument with 2 of his friends. Now he no longer considers them as friends. On his way back home, he made one more friend. So how many friends does James have left?"""
    # Define the initial number of friends
    num_friends = 20

    # Subtract the number of friends he lost in the argument
    num_friends -= 2

    # Add the new friend he made on his way back home
    num_friends += 1

    # return the result
    result = num_friends
    return result

print(solution())