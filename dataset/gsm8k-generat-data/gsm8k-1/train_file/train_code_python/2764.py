def solution():
    """Saturday at the ice cream shop, there were twice as many people who ordered vanilla ice cream as ordered chocolate ice cream. If 220 people ordered ice cream on Saturday, and 20% of those ordered vanilla ice cream, how many people ordered chocolate ice cream?"""
    total_orders = 220
    vanilla_percent = 20
    vanilla_orders = total_orders * (vanilla_percent / 100)
    chocolate_orders = (total_orders - vanilla_orders) / 3
    result = chocolate_orders
    return result

print(solution())