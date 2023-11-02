def solution():
    wellington_population = 900  # Wellington has a population of 900
    port_perry_population = wellington_population * 7  # Port Perry has seven times the population of Wellington
    lazy_harbor_population = port_perry_population - 800  # Port Perry has 800 more people than Lazy Harbor

    # Calculate the total population of Port Perry and Lazy Harbor combined
    total_population = port_perry_population + lazy_harbor_population
    result = total_population
    return result

print(solution())