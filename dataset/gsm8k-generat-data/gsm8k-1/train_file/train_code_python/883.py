def solution():
    """Two vampires have come to the sleepy village of Willowton, population 300. Every night, each vampire turns 5 more people into vampires. How many vampires are there after two nights?"""
    initial_population = 300
    vampires_per_vampire = 5
    total_vampires = initial_population + 2 * (2 * vampires_per_vampire)
    result = total_vampires
    return result

print(solution())