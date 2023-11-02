def solution():
    """Apple sold 100 iPhones at their New York store today for an average cost of $1000. They also sold 20 iPads for an average cost of $900 and 80 Apple TVs for an average cost of $200. What was the average cost across all products sold today?"""
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