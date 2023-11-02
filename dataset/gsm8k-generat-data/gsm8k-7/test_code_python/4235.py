def solution():
    num_new_people = 100
    num_leaving = 400
    num_years = 4
    final_population = 60

    # Calculate the population after the original people move out and the new people move in
    population = final_population * 2 ** num_years + num_leaving - num_new_people

    # Calculate the number of original population before new people moved in
    original_population = population - num_new_people
    result = original_population
    return result

print(solution())