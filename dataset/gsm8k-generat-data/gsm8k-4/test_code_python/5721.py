def solution():
    """Chenny has 10 pieces of candies to be given out to her friends. She realized that she needs to buy 4 more so each of her friends will receive 2 candies. How many friends does Chenny have?"""
    # Define the initial number of candies and the number of candies needed for each friend
    initial_candies = 10
    candies_per_friend = 2

    # Calculate the total number of candies needed
    total_candies_needed = initial_candies + 4

    # Calculate the number of friends
    num_friends = total_candies_needed // candies_per_friend

    # Return the result
    result = num_friends
    return result

print(solution())