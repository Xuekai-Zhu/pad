def solution():
    initial_bunnies = 30
    bunnies_given_away = initial_bunnies * 2/5
    bunnies_left = initial_bunnies - bunnies_given_away
    bunnies_born = bunnies_left * 2
    total_bunnies = bunnies_left + bunnies_born
    
    return total_bunnies

print(solution())