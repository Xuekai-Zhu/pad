def solution():
    """
    The population of an area starts at 100,000 people.  It increases by 60% over 10 years due to birth.  In that same time, 
    2000 people leave per year from emigration and 2500 people come in per year from immigration.  How many people are in the 
    area at the end of 10 years?
    """
    
    # define the initial population
    population = 100000
    
    # calculate the population increase due to birth over 10 years
    population_increase = population * 0.6
    
    # calculate the total population after 10 years due to birth
    population += population_increase
    
    # calculate the net population increase due to immigration and emigration over 10 years
    immigration_increase = 2500 - 2000
    net_population_increase = immigration_increase * 10
    
    # add the net population increase to the total population after 10 years due to birth
    population += net_population_increase
    
    # display the final population
    result = population
    return result

print(solution())