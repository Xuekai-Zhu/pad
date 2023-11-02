def solution():
    repair_1_revenue = 20 * 300
    repair_1_cost = 5 * 300
    repair_2_revenue = 300 * 2
    repair_2_cost = 50 * 2
    retail_revenue = 2000
    fixed_expenses = 4000
    repair_profit = (repair_1_revenue - repair_1_cost) + (repair_2_revenue - repair_2_cost)
    total_profit = repair_profit + retail_revenue - fixed_expenses
    result = total_profit
    
    return result

print(solution())