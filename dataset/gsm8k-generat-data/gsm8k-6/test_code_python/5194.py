def solution():
    cost_per_patch = 1.25  # cost per patch ordered in units of 100
    selling_price_per_100 = 1200  # selling price for 100 patches
    profit_per_100 = selling_price_per_100 - (100 * cost_per_patch)  # profit per 100 patches sold
    net_profit = profit_per_100 / 100  # net profit per patch sold
    result = net_profit
    return result

print(solution())