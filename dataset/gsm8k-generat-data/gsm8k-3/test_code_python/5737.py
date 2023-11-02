def solution():
    """Paula has 20 candies to be given out to her six friends. She needs to buy four additional candies so she can give an equal number of candies to her friends. How many candies will each of her friends get?"""
    # Define the initial number of candies
    initial_candies = 20

    # Define the additional candies needed
    additional_candies = 4

    # Define the total number of candies
    total_candies = initial_candies + additional_candies

    # Define the number of friends
    num_friends = 6

    # Calculate the number of candies each friend will get
    candies_per_friend = total_candies // num_friends

    # Display the number of candies each friend will get
    result = candies_per_friend
    return result

print(solution())