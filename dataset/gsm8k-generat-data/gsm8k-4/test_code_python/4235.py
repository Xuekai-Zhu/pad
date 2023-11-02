def solution():
    """After 100 new people move into a town, 400 of the original population move out. Every year afterward, the town’s population is halved. After 4 years, the population is 60 people. Before the new people moved in, how many people lived in the town?"""
    # Define the initial population and the number of new people
    initial_population = None
    new_people = 100

    # Calculate the population after the new people move in and 400 of the original population move out
    population = initial_population + new_people - 400

    # Calculate the population after 4 years of halving
    for i in range(4):
        population /= 2

    # Solve for the initial population
    initial_population = population * 2 + 400

    result = initial_population
    return result

print(solution())