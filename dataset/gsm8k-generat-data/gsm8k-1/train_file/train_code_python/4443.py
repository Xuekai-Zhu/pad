def solution():
    """The population of Port Perry is seven times as many as the population of Wellington. The population of Port Perry is 800 more than the population of Lazy Harbor. If Wellington has a population of 900, how many people live in Port Perry and Lazy Harbor combined?"""
    wellington_population = 900
    port_perry_population = wellington_population * 7
    lazy_harbor_population = port_perry_population - 800
    total_population = port_perry_population + lazy_harbor_population
    result = total_population
    return result

print(solution())