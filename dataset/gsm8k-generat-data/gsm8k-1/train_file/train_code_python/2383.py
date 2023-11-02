def solution():
    """Gerald wants to buy a meat pie that costs 2 pfennigs. Gerald has 54 farthings, and there are 6 farthings to a pfennig. How many pfennigs will Gerald have left after buying the pie?"""
    pie_cost = 2
    farthings_owned = 54
    farthings_per_pfennig = 6
    total_pfennigs_owned = farthings_owned // farthings_per_pfennig
    pfennigs_left = total_pfennigs_owned - pie_cost
    result = pfennigs_left
    return result

print(solution())