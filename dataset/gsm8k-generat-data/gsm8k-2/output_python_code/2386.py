def solution():
    """Dirk sells amulets at a Ren Faire. He sells for 2 days and each day he sells 25 amulets. Each amulet sells for 40 dollars and they cost him 30 dollars to make. If he has to give 10% of his revenue to the faire, how much profit did he make?"""
    num_days = 2
    amulets_per_day = 25
    sale_price = 40
    cost_price = 30
    faire_percent = 0.1

    total_sales = num_days * amulets_per_day * sale_price
    total_cost = num_days * amulets_per_day * cost_price
    faire_cut = total_sales * faire_percent
    profit = total_sales - total_cost - faire_cut
    result = profit
    return result

print(solution())