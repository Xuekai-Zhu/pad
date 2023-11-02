def solution():
    candies = 20
    friends = 6
    candies_needed = 4
    total_candies = candies + candies_needed
    candies_per_friend = total_candies / friends
    result = candies_per_friend
    return result

print(solution())