def solution():
    
    passes_cost = 100
    oldest_son_visits = 35
    youngest_son_visits = 15
    total_passes_cost = passes_cost * 2
    total_visits = oldest_son_visits + youngest_son_visits
    cost_per_trip = total_passes_cost / total_visits
    result = cost_per_trip
    return result

print(solution())