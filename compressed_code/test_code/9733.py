def solution():
    
    num_sweaters = 6
    num_scarves = 6
    sweater_cost = 30
    scarf_cost = 20
    total_cost = (num_sweaters * sweater_cost) + (num_scarves * scarf_cost)
    remaining_savings = 500 - total_cost
    result = remaining_savings
    return result

print(solution())