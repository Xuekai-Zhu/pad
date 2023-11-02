def solution():
    
    nellie_candies = 12
    jacob_candies = nellie_candies / 2
    lana_candies = jacob_candies - 3
    total_candies = 30
    total_eaten = nellie_candies + jacob_candies + lana_candies
    remaining_candies = total_candies - total_eaten
    candies_per_person = remaining_candies / 3
    result = candies_per_person
    return result

print(solution())