def solution():
    
    initial_bunnies = 30
    matured_bunnies = initial_bunnies
    given_bunnies = 2/5 * matured_bunnies
    remaining_bunnies = matured_bunnies - given_bunnies
    newborn_kittens = remaining_bunnies * 2
    total_bunnies = remaining_bunnies + newborn_kittens
    result = total_bunnies
    return result

print(solution())