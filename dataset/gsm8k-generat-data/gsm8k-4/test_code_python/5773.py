def solution():
    """The Ravenswood forest has four times as many gnomes as the Westerville woods. If there are 20 gnomes in Westerville woods, how many gnomes would remain in Ravenswood forest if 40% of the gnomes are taken for use by the forest owner?"""
    # Calculate the number of gnomes in Ravenswood forest
    ravenswood_gnomes = 4 * 20

    # Calculate the number of gnomes taken by the forest owner
    taken_gnomes = ravenswood_gnomes * 0.4

    # Calculate the number of gnomes remaining in Ravenswood forest
    remaining_gnomes = ravenswood_gnomes - taken_gnomes

    # return the result
    result = remaining_gnomes
    return result

print(solution())