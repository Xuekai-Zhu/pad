def solution():
     mr_banks_investments = 8
     mr_banks_revenue = 500
     ms_elizabeth_investments = 5
     ms_elizabeth_revenue = 900
     total_revenue_mr_banks = mr_banks_investments * mr_banks_revenue
     total_revenue_ms_elizabeth = ms_elizabeth_investments * ms_elizabeth_revenue
     difference = total_revenue_ms_elizabeth - total_revenue_mr_banks
     result = difference
     return result

print(solution())