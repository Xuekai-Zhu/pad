def solution():
    total_people = 38
    beaver_ratio = 19
    moose_ratio = 2
    beavers = total_people / beaver_ratio
    moose = beavers / moose_ratio
    moose_population = moose / 1000000
    result = moose_population
    return result

print(solution())