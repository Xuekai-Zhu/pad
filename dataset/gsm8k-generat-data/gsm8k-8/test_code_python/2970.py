def solution():
    # Calculate the number of female bunnies that matured after four months
    mature_bunnies = 30 * (3/4)

    # Calculate the number of mature female bunnies that Rodney received
    rodney_bunnies = mature_bunnies * (2/5)

    # Calculate the total number of bunnies after three more months
    total_bunnies = mature_bunnies - rodney_bunnies + (2 * mature_bunnies)

    result = total_bunnies
    return result

print(solution())