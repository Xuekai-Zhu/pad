def solution():
    
    cotton_candies = 50
    candies_given = 2 * 5
    candies_remaining = cotton_candies - candies_given
    candies_given_cousin = candies_remaining / 4
    candies_remaining -= candies_given_cousin
    candies_remaining -= 12
    result = candies_remaining
    return result

print(solution())