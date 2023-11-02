def solution():
    Shelly_candies = 20
    friend_candies = 2 * Shelly_candies
    total_candies = Shelly_candies + friend_candies
    friend_candies_eaten = 10
    friend_candies_left = total_candies - friend_candies_eaten
    result = friend_candies_left
    
    return result

print(solution())