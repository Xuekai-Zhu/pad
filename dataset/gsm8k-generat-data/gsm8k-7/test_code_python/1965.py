def solution():
    statues_year1 = 4
    statues_year2 = statues_year1 * 4
    statues_year3 = statues_year2 + 12 - 3
    statues_broken_year3 = 3
    statues_new_year4 = 2 * statues_broken_year3

    total_statues = statues_year1 + statues_year2 + statues_year3 + statues_new_year4
    result = total_statues
    return result

print(solution())