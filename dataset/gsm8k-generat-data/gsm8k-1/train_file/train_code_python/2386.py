def solution():
    """Dirk sells amulets at a Ren Faire. He sells for 2 days and each day he sells 25 amulets. Each amulet sells for 40 dollars and they cost him 30 dollars to make. If he has to give 10% of his revenue to the faire, how much profit did he make?"""
    days_selling = 2
    amulets_per_day = 25
    sale_price = 40
    cost_to_make = 30
    faire_cut = 0.1
    revenue = days_selling * amulets_per_day * sale_price
    cost = days_selling * amulets_per_day * cost_to_make
    profit_before_faire_cut = revenue - cost
    profit = profit_before_faire_cut * (1 - faire_cut)
    result = profit
    return result

print(solution())