def solution():
    population = 300000
    immigrants = 50000
    emigrants = 30000

    # Calculate the new population after immigration and emigration
    new_population = population + immigrants - emigrants

    # Calculate the number of people who get pregnant
    pregnant = new_population / 8

    # Calculate the number of people who have twins
    twins = pregnant / 4

    # Calculate the final population after the births
    final_population = new_population + twins

    result = final_population
    return result

print(solution())