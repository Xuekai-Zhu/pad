def solution():
    """If you buy a dozen of doughnuts, it costs $8; but if you buy 2 dozens, it costs $14. How much will you save from buying 3 sets of 2 dozens than buying 6 sets of 1 dozen?"""
    cost_1dozen = 8
    cost_2dozen = 14
    cost_6sets_1dozen = 6 * cost_1dozen
    cost_3sets_2dozen = 3 * cost_2dozen
    savings = cost_6sets_1dozen - cost_3sets_2dozen
    result = savings
    return result

print(solution())