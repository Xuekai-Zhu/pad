def solution():
    # Determine the number of candies each person can eat before crying
    nellie_candies = 12
    jacob_candies = nellie_candies / 2
    lana_candies = jacob_candies - 3

    # Determine the total number of candies they ate before crying
    total_candies_eaten = nellie_candies + jacob_candies + lana_candies

    # Determine the number of candies left in the bucket
    candies_left = 30 - total_candies_eaten

    # Determine the number of candies each person gets after dividing the remaining candies equally
    candies_per_person = candies_left / 3

    result = candies_per_person
    return result

print(solution())