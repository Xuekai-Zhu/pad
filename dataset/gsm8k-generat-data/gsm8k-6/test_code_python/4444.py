def solution():
    # Find the population of Port Perry and Lazy Harbor
    population_Wellington = 900
    population_PortPerry = 7 * population_Wellington
    population_LazyHarbor = population_PortPerry - 800

    # Find the total population of Port Perry and Lazy Harbor combined
    total_population = population_PortPerry + population_LazyHarbor
    result = total_population
    return result

print(solution())