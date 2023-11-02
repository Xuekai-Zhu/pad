def solution():
   Josh_has_candies = 100
    given_to_siblings = 3 * 10
    half_of_remaining = (Josh_has_candies - given_to_siblings) / 2
    Josh_wants_to_eat = 16
    candies_left = Josh_has_candies - given_to_siblings - half_of_remaining - Josh_wants_to_eat
    result = candies_left
    
    return result

print(solution())