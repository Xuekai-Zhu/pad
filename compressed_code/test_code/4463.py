def solution():
    
    westerville_gnomes = 20
    ravenswood_gnomes = 4 * westerville_gnomes
    taken_gnomes = 0.4 * ravenswood_gnomes
    remaining_gnomes = ravenswood_gnomes - taken_gnomes
    result = remaining_gnomes
    return result

print(solution())