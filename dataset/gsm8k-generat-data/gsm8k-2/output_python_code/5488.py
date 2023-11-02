def solution():
    """Kirsty collects small models of animals. The last time she bought some, each one cost $0.45. She saves enough to buy 30 models, but when she goes to the shop, she finds out that the price had increased to $0.50. How many models can she buy now?"""
    saved_money = 30 * 0.45
    new_price = 0.50
    models_can_buy = saved_money / new_price
    result = models_can_buy
    return result

print(solution())