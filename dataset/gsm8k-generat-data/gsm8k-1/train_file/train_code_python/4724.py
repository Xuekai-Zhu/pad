def solution():
    """In Canada, for every moose there are two beavers, and for every beaver there are 19 humans. If there are 38 million people in Canada, what is the moose population of Canada, in millions?"""
    total_humans = 38000000
    beavers_per_human = 1/19
    moose_per_beaver = 1/2
    moose_population = total_humans * beavers_per_human * moose_per_beaver
    result = moose_population / 1000000
    return result

print(solution())