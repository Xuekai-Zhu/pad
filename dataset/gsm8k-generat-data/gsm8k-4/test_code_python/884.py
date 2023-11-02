def solution():
    """Two vampires have come to the sleepy village of Willowton, population 300. Every night, each vampire turns 5 more people into vampires. How many vampires are there after two nights?"""
    # Define the initial number of vampires and population
    initial_vampires = 2
    population = 300

    # Calculate the number of total vampires after two nights
    total_vampires = (initial_vampires * (5 * 2 + 1)) ** 2

    result = total_vampires
    return result

print(solution())