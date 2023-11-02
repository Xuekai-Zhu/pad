def solution():
    # Calculate the number of ducks
    ducks = 20 * 0.5  # 50% more ducks than cows

    # Calculate the total number of ducks and cows
    total_animals = ducks + 20

    # Calculate the number of pigs
    pigs = total_animals // 5

    # Calculate the total number of animals
    total_animals += pigs

    result = total_animals
    return result

print(solution())