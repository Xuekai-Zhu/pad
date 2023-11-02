def solution():
    initial_bunnies = 30

    # Calculate the number of bunnies that matured after 4 months
    mature_bunnies = initial_bunnies

    # Calculate the number of bunnies that Marlon gave to Rodney
    given_bunnies = (2/5) * mature_bunnies

    # Calculate the number of remaining bunnies
    remaining_bunnies = mature_bunnies - given_bunnies

    # Calculate the number of bunnies after giving birth to kittens
    total_bunnies = remaining_bunnies + (2 * remaining_bunnies)

    result = total_bunnies
    return result

print(solution())