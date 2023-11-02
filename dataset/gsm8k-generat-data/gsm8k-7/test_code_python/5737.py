def solution():
    total_candies = 20
    num_friends = 6
    additional_candies = 4

    # Calculate the total number of candies after buying additional candies
    total_candies = total_candies + additional_candies

    # Calculate the number of candies each friend will get
    num_candies_per_friend = total_candies // num_friends
    result = num_candies_per_friend
    return result

print(solution())