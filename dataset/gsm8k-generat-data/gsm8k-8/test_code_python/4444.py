def solution():
    #Define the population of Wellington
    wellington_population = 900
    
    #Calculate the population of Port Perry
    port_perry_population = 7 * wellington_population + 800
    
    #Calculate the population of Lazy Harbor
    lazy_harbor_population = port_perry_population - 800
    
    #Calculate the total population of Port Perry and Lazy Harbor combined
    total_population = port_perry_population + lazy_harbor_population
    
    result = total_population
    return result

print(solution())