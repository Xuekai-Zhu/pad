def solution():
    season_pass_cost = 100.00
    visits_by_oldest_son = 35
    visits_by_youngest_son = 15
    total_visits = visits_by_oldest_son + visits_by_youngest_son
    cost_per_visit = season_pass_cost / total_visits
    return cost_per_visit

print(solution())