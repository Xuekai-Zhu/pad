def solution():
    haircut_price = 30
    perm_price = 40
    dye_job_price = 60
    tips = 50
    dye_job_cost = 2 * 10
    total_revenue = haircut_price * 4 + perm_price + dye_job_price * 2 - dye_job_cost
    total_profit = total_revenue + tips
    result = total_profit
    
    return result

print(solution())