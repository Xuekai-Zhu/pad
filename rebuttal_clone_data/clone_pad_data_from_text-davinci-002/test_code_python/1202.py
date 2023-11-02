def solution():
    total_monthly_cost_1 = 800 + 260 + (58 * 31 * 20)
    total_monthly_cost_2 = 900 + 200 + (58 * 21 * 20)
    difference = total_monthly_cost_1 - total_monthly_cost_2
    result = difference
    return result

print(solution())