def solution():
    """After 100 new people move into a town, 400 of the original population move out. Every year afterward, the town’s population is halved. After 4 years, the population is 60 people. Before the new people moved in, how many people lived in the town?"""
    final_population = 60
    years_passed = 4
    population_after_move_out = final_population * 2**years_passed
    population_before_move_out = population_after_move_out + 400 - 100
    result = population_before_move_out
    return result

print(solution())