def solution():
    """Five less than three times the number of Doberman puppies plus the difference between the number of Doberman puppies and the number of Schnauzers is equal to 90. If the number of Doberman puppies is 20, how many Schnauzers are there?"""
    doberman_puppies = 20
    equation_result = 90
    schnauzers = (equation_result - 5 - (3 * doberman_puppies)) / 2
    result = schnauzers
    return result

print(solution())