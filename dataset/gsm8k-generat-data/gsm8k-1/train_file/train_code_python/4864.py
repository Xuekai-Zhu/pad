def solution():
    """A city has a population of 300,000. 50,000 people immigrate to the country and then 30,000 people leave. 
    After that 1/8 of the population gets pregnant and 1/4 of those people have twins. 
    How many people are there after the births?"""
    
    population = 300000
    immigration = 50000
    emigration = 30000
    new_population = population + immigration - emigration
    pregnancies = new_population / 8
    twins = pregnancies / 4
    total_population = new_population + twins
    result = total_population
    return result

print(solution())