def solution():
    candies = 10
    to_buy = 4
    total_candies = candies + to_buy
    candies_per_friend = 2
    num_friends = total_candies // candies_per_friend
    result = num_friends
    return result

print(solution())