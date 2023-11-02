def solution():
    """Mrs. Choi purchased a house for $80000. Five years later, she sold it for a 20% profit and got a 5% broker's commission from the original price. How much did the house sell for?"""
    original_price = 80000
    profit_percent = 20
    broker_commission_percent = 5
    selling_price = original_price + (original_price * profit_percent / 100)
    broker_commission = original_price * broker_commission_percent / 100
    net_selling_price = selling_price - broker_commission
    result = net_selling_price
    return result

print(solution())