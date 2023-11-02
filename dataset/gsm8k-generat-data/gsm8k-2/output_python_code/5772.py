def solution():
    """The Ravenswood forest has four times as many gnomes as the Westerville woods. If there are 20 gnomes in Westerville woods, how many gnomes would remain in Ravenswood forest if 40% of the gnomes are taken for use by the forest owner?"""
    westerville_gnomes = 20
    ravenswood_gnomes = 4 * westerville_gnomes
    taken_gnomes = 0.4 * ravenswood_gnomes
    remaining_gnomes = ravenswood_gnomes - taken_gnomes
    result = remaining_gnomes
    return result

print(solution())