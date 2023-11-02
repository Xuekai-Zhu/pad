def solution():
    
    total_candies = 100
    siblings_candies = 3 * 10
    remaining_candies = total_candies - siblings_candies
    friend_candies = remaining_candies / 2
    josh_candies = 16
    candies_left = remaining_candies - friend_candies - josh_candies
    result = candies_left
    return result

print(solution())