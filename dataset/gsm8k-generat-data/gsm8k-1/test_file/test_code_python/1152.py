def solution():
    """Linus works for a trading company. He buys a mobile device for $20 and sells it for twice the amount of the original price. If he bought 2 devices last Monday and 4 devices last Tuesday, how much profit was he able to earn after selling all the mobile devices he bought last Monday and Tuesday?"""
    purchase_price = 20
    selling_price = 2 * purchase_price
    devices_bought_mon = 2
    devices_bought_tue = 4
    total_cost = (devices_bought_mon + devices_bought_tue) * purchase_price
    total_revenue = (devices_bought_mon + devices_bought_tue) * selling_price
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())