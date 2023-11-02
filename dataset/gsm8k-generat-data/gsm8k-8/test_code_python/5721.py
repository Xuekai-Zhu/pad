def solution():
    # Define the number of initial candies
    initial_candies = 10

    # Define the desired number of candies per friend
    desired_candies_per_friend = 2

    # Calculate the number of friends
    num_friends = (initial_candies + 4) / desired_candies_per_friend
    result = num_friends
    return result

print(solution())