def solution():
    mining_profit_per_month = 3_000_000 * 30
    refining_profit_per_month = 5_000_000 * 30
    total_profit_per_month = mining_profit_per_month + refining_profit_per_month - 30_000_000
    fine_percentage = 0.01
    fine_amount = total_profit_per_month * fine_percentage
    result = fine_amount
    return result

print(solution())