def solution():
    pacific_war_start = 1941
    pacific_war_end = 1945
    musket_obsolete_year = 1870
    if musket_obsolete_year > pacific_war_start:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())