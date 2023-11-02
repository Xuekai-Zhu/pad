def solution():
    """After 100 new people move into a town, 400 of the original population move out. Every year afterward, the town’s population is halved. After 4 years, the population is 60 people. Before the new people moved in, how many people lived in the town?"""
    new_people = 100
    population_change = -400
    years = 4
    final_population = 60
    population_after_new = final_population * (2 ** years)
    original_population = (population_after_new - new_people - population_change)
    result = original_population
    return result

print(solution())