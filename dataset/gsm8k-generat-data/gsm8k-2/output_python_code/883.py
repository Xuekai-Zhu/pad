def solution():
    """Two vampires have come to the sleepy village of Willowton, population 300. Every night, each vampire turns 5 more people into vampires. How many vampires are there after two nights?"""
    starting_vampires = 2
    population = 300
    first_night_turned = starting_vampires * (5 + 1)
    second_night_turned = first_night_turned * (5 + 1)
    total_vampires = starting_vampires + first_night_turned + second_night_turned
    result = total_vampires
    return result

print(solution())