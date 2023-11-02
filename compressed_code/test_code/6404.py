def solution():
    
    red_candies = 40
    yellow_candies = (3*red_candies) - 20
    blue_candies = yellow_candies / 2
    total_candies = red_candies + yellow_candies + blue_candies
    remaining_candies = total_candies - yellow_candies
    result = remaining_candies
    return result

print(solution())