def solution():
    population_wellington = 900
    population_portperry = 7 * population_wellington
    population_lazyharbor = population_portperry - 800

    # Calculate the total population of Port Perry and Lazy Harbor combined
    total_population = population_portperry + population_lazyharbor
    result = total_population
    return result

print(solution())