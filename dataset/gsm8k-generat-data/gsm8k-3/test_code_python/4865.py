def solution():
    """A city has a population of 300,000.  50,000 people immigrate to the country and then 30,000 people leave.  After that 1/8 of the population gets pregnant and 1/4 of those people have twins.  How many people are there after the births?"""
    # Define the initial population
    population = 300000

    # Calculate the new population after immigration and emigration
    population = population + 50000 - 30000

    # Calculate the number of pregnant individuals and the number of twins born
    pregnant = population // 8
    twins = pregnant // 4

    # Calculate the new population after the births
    population = population + twins

    # Display the new population
    result = population
    return result

print(solution())