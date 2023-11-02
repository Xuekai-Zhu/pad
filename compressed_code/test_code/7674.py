def solution():
    
    pie_cost = 2
    farthings_owned = 54
    farthings_per_pfennig = 6
    total_pfennigs_owned = farthings_owned // farthings_per_pfennig
    pfennigs_left = total_pfennigs_owned - pie_cost
    result = pfennigs_left
    return result

print(solution())