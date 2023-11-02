def solution():
    cows = 20
    ducks = round(cows * 1.5)  # Philip has 50% more ducks than cows
    total_animals = cows + ducks  # Total number of cows and ducks

    pigs = round(total_animals / 5)  # Philip has as many pigs as one-fifth of cows and ducks in total

    # Calculate the total number of animals on Philip's farm
    total_animals = cows + ducks + pigs
    result = total_animals
    return result

print(solution())