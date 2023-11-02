def solution():
    """The population of Port Perry is seven times as many as the population of Wellington. The population of Port Perry is 800 more than the population of Lazy Harbor. If Wellington has a population of 900, how many people live in Port Perry and Lazy Harbor combined?"""
    # Define the population of Wellington
    wellington_population = 900

    # Calculate the population of Port Perry
    port_perry_population = wellington_population * 7

    # Calculate the population of Lazy Harbor
    lazy_harbor_population = port_perry_population - 800

    # Calculate the total population of Port Perry and Lazy Harbor combined
    total_population = port_perry_population + lazy_harbor_population

    # Display the total population
    result = total_population
    return result

print(solution())