def solution():
    """Nellie can eat 12 sourball candies before crying. Jacob can only manage half of that number of candies, and Lana can only do three fewer than Jacob. They had a bucket of 30 candies, and all of them ate until they cried. If they divide the remaining candies in the bucket equally, how many sourball candies will they each get?"""
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