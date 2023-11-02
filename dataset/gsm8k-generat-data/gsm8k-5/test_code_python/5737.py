def solution():
    total_candies = 20 + 4  # Paula has 20 candies and needs to buy 4 more
    num_friends = 6  # Paula has 6 friends to give the candies to

    # Divide the total number of candies by the number of friends to get the number of candies each friend will get
    candies_per_friend = total_candies / num_friends
    result = candies_per_friend
    return result

print(solution())