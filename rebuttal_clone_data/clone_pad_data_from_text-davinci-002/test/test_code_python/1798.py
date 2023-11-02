def solution():
    candies_mark = 30
    candies_peter = 25
    candies_john = 35
    total_candies = candies_mark + candies_peter + candies_john
    candies_per_person = total_candies / 3
    result = candies_per_person
    return result

print(solution())