def solution():
    # Define the initial population
    population = 300000

    # Calculate the new population after immigration and emigration
    population += 50000
    population -= 30000

    # Calculate the number of pregnant women and the number of births
    pregnant_women = population / 8
    twin_births = pregnant_women / 4

    # Calculate the final population
    population += twin_births * 2
    result = population
    return result

print(solution())