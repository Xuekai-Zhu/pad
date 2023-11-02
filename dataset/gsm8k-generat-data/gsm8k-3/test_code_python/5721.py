def solution():
    """Chenny has 10 pieces of candies to be given out to her friends. She realized that she needs to buy 4 more so each of her friends will receive 2 candies. How many friends does Chenny have?"""
    # Calculate the total number of candies needed
    total_candies = 10 + 4

    # Calculate the number of friends that can receive 2 candies each
    num_friends = total_candies // 2

    # Display the number of friends Chenny has
    result = num_friends
    return result

print(solution())