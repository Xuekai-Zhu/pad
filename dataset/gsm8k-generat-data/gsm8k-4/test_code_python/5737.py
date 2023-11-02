def solution():
    """Paula has 20 candies to be given out to her six friends. She needs to buy four additional candies so she can give an equal number of candies to her friends. How many candies will each of her friends get?"""
    # Define the initial number of candies and friends
    candies = 20
    friends = 6

    # Calculate the total number of candies needed
    total_candies = candies + 4

    # Calculate the number of candies each friend will get
    candies_per_friend = total_candies // friends

    # return the result
    result = candies_per_friend
    return result

print(solution())