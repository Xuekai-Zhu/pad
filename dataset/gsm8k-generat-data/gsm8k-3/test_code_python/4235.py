def solution():
    """After 100 new people move into a town, 400 of the original population move out. Every year afterward, the town’s population is halved. After 4 years, the population is 60 people. Before the new people moved in, how many people lived in the town?"""
    # Let x be the original population
    # After the new people move in, the population becomes x+100
    # After 400 people move out, the population becomes x+100-400 = x-300
    # After 4 years, the population becomes (x-300)/2^4 = 60
    # Simplifying, (x-300) = 60 * 2^4 = 960
    # Solving for x, x = 1260

    # Therefore, before the new people moved in, there were 1260 people in the town.
    result = 1260
    return result

print(solution())