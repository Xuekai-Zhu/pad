def solution():
    """Gerald wants to buy a meat pie that costs 2 pfennigs. Gerald has 54 farthings, and there are 6 farthings to a pfennig. How many pfennigs will Gerald have left after buying the pie?"""
    pie_cost_pfennigs = 2
    total_farthings = 54
    farthings_per_pfennig = 6
    total_pfennigs = total_farthings // farthings_per_pfennig
    remaining_pfennigs = total_pfennigs - pie_cost_pfennigs
    result = remaining_pfennigs
    return result

print(solution())