def solution():
    """The Ravenswood forest has four times as many gnomes as the Westerville woods. If there are 20 gnomes in Westerville woods, how many gnomes would remain in Ravenswood forest if 40% of the gnomes are taken for use by the forest owner?"""
    gnomes_in_westerville = 20
    gnomes_in_ravenswood = gnomes_in_westerville * 4
    gnomes_taken = gnomes_in_ravenswood * 0.4
    gnomes_remaining = gnomes_in_ravenswood - gnomes_taken
    result = gnomes_remaining
    return result

print(solution())