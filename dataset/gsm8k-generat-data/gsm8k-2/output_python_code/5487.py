def solution():
    """The population of Delaware is 974,000. A study showed that there are 673 cell phones per 1000 people in the state. How many cell phones are there in Delaware?"""
    population = 974000
    cell_phones_per_1000 = 673
    total_cell_phones = (population * cell_phones_per_1000) / 1000
    result = total_cell_phones
    return result

print(solution())