def solution():
    
    total_cotton_candies = 50
    candies_given_to_siblings = 2 * 5
    remaining_candies = total_cotton_candies - candies_given_to_siblings
    candies_given_to_cousin = remaining_candies // 4
    remaining_candies = remaining_candies - candies_given_to_cousin - 12
    result = remaining_candies
    return result

print(solution())