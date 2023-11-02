def solution():
    """In the first round of bowling, Patrick knocked down a total of 70 pins and Richard knocked down 15 more pins than Patrick. In the second round, Patrick knocked down twice as many pins as Richard in the first round and Richard knocked down 3 less than Patrick. How many more pins in total did Richard knock down than Patrick?"""
    patrick_first = 70
    richard_first = patrick_first + 15
    patrick_second = 2 * richard_first
    richard_second = patrick_first - 3
    patrick_total = patrick_first + patrick_second
    richard_total = richard_first + richard_second
    difference = richard_total - patrick_total
    result = difference
    return result

print(solution())