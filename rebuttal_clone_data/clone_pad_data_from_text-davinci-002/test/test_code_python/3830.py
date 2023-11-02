def solution():
    cost_per_pie = 5
    slices_per_pie = 4
    pies_sold = 9
    total_slices_sold = pies_sold * slices_per_pie
    total_cost = pies_sold * cost_per_pie
    total_revenue = total_slices_sold * cost_per_pie
    result = total_revenue
    return result

print(solution())