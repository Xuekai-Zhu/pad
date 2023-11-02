def solution():
    """If you buy a dozen of doughnuts, it costs $8; but if you buy 2 dozens, it costs $14. How much will you save from buying 3 sets of 2 dozens than buying 6 sets of 1 dozen?"""
    single_dozen_cost = 8
    double_dozen_cost = 14
    set_of_two_cost = 2 * double_dozen_cost
    set_of_one_cost = 6 * single_dozen_cost
    saving = set_of_one_cost - set_of_two_cost * 3
    result = saving
    return result

print(solution())