def solution():
    
    total_candies = 100
    josh_siblings = 3
    candies_per_siblings = 10
    candies_given_to_siblings = josh_siblings * candies_per_siblings
    candies_remaining = total_candies - candies_given_to_siblings
    candies_given_to_friend = candies_remaining / 2
    josh_candies_remaining = candies_remaining - candies_given_to_friend - 16
    result = josh_candies_remaining
    return result

print(solution())