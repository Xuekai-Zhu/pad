def solution():
    """In Canada, for every moose there are two beavers, and for every beaver there are 19 humans. If there are 38 million people in Canada, what is the moose population of Canada, in millions?"""
    human_population = 38000000
    beaver_population = human_population / 19
    moose_population = beaver_population / 2
    result = moose_population / 1000000
    return result

print(solution())