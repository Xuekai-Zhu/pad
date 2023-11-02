def solution():
    """ Marlon had 30 female baby bunnies in his hutch. They matured after four months, and he gave 2/5 of them to his friend Rodney. If after another three months the bunnies conceived and gave birth to 2 kittens each, calculate the total number of bunnies Marlon has in his hutch now."""
    initial_bunnies = 30
    matured_bunnies = initial_bunnies
    given_bunnies = 2/5 * matured_bunnies
    remaining_bunnies = matured_bunnies - given_bunnies
    newborn_kittens = remaining_bunnies * 2
    total_bunnies = remaining_bunnies + newborn_kittens
    result = total_bunnies
    return result

print(solution())