def solution():
    """A local school is holding a food drive. Mark brings in 4 times as many cans as Jaydon. Jaydon brings in 5 more than twice the amount of cans that Rachel brought in. If there are 135 cans total, how many cans did Mark bring in?"""
    total_cans = 135
    rachel_cans = (total_cans - 5) / 2
    jaydon_cans = rachel_cans + 5
    mark_cans = 4 * jaydon_cans
    result = mark_cans
    return result

print(solution())