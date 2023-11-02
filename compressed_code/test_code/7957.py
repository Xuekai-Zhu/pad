def solution():
    
    total_candies = 300
    sour_candies_percentage = 40
    good_candies = total_candies * (100 - sour_candies_percentage) / 100
    candies_each = good_candies / 3
    result = candies_each
    return result

print(solution())