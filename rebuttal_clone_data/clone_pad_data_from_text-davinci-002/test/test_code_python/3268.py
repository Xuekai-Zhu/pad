def solution():
    westerville_woods = 20
    ravenswood_forest = westerville_woods * 4
    forest_owner = .4
    total_gnomes = ravenswood_forest - (ravenswood_forest * forest_owner)
    result = total_gnomes
    return result

print(solution())