def solution():
    days_selling = 2
    amulets_sold_per_day = 25
    sale_price_per_amulet = 40
    cost_to_make_amulet = 30
    revenue = days_selling * amulets_sold_per_day * sale_price_per_amulet
    faire_cut = revenue * 0.1
    profit = revenue - faire_cut - (days_selling * amulets_sold_per_day * cost_to_make_amulet)
    result = profit
    return result

print(solution())