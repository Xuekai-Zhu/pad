def solution():
    cost_child = 3
    cost_adult = 4
    monday_children = 7
    monday_adults = 5
    monday_total = cost_child * monday_children + cost_adult * monday_adults
    tuesday_children = 4
    tuesday_adults = 2
    tuesday_total = cost_child * tuesday_children + cost_adult * tuesday_adults
    total_revenue = monday_total + tuesday_total
    result = total_revenue
    
    return result

print(solution())