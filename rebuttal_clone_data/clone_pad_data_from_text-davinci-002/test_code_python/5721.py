def solution():
    total_candies = 10
    candies_per_friend = 2
    total_needed = total_candies + (candies_per_friend * 4)
    total_friends = total_needed / candies_per_friend
    result = total_friends
    return result

print(solution())