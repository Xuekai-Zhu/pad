def solution():
    
    yellow_candies = (40 * 3) - 20
    blue_candies = yellow_candies / 2
    total_candies = 40 + yellow_candies + blue_candies
    eaten_candies = yellow_candies
    candies_left = total_candies - eaten_candies
    result = candies_left
    
    return result

print(solution())