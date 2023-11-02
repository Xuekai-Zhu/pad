def solution():
    
    num_iphones = 100
    avg_cost_iphones = 1000
    num_ipads = 20
    avg_cost_ipads = 900
    num_tvs = 80
    avg_cost_tvs = 200
    total_sales = (num_iphones * avg_cost_iphones) + (num_ipads * avg_cost_ipads) + (num_tvs * avg_cost_tvs)
    total_items_sold = num_iphones + num_ipads + num_tvs
    avg_cost = total_sales / total_items_sold
    result = avg_cost
    return result

print(solution())