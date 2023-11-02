def solution():
    nellie_candies = 12
    jacob_candies = nellie_candies / 2
    lana_candies = jacob_candies - 3

    total_candies = 30
    remaining_candies = total_candies - (nellie_candies + jacob_candies + lana_candies)

    num_people = 3
    candies_per_person = remaining_candies / num_people
    result = candies_per_person
    return result

print(solution())