def solution():
    """Hannah's family has ten pigs on their farm. They also have three fewer than twice as many cows as pigs and six more goats than cows. How many animals do they have on their farm?"""
    pigs = 10
    cows = (2 * pigs) - 3
    goats = cows + 6
    total_animals = pigs + cows + goats
    result = total_animals
    return result

print(solution())