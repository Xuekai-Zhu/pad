def solution():
    nellie_candies = 12
    jacob_candies = nellie_candies / 2
    lana_candies = jacob_candies - 3
    total_candies = nellie_candies + jacob_candies + lana_candies
    remainder = 30 - total_candies
    result = remainder / 3
    return result

print(solution())