def solution():
    """Mrs. Choi purchased a house for $80000. Five years later, she sold it for a 20% profit and got a 5% broker's commission from the original price. How much did the house sell for?"""
    purchase_price = 80000
    profit_percentage = 20
    broker_commission_percentage = 5
    
    # calculate profit amount
    profit_amount = purchase_price * (profit_percentage / 100)
    
    # calculate sale price
    sale_price = purchase_price + profit_amount
    
    # calculate broker's commission
    broker_commission = purchase_price * (broker_commission_percentage / 100)
    
    # calculate final sale price with commission
    final_sale_price = sale_price - broker_commission
    
    result = final_sale_price
    return result

print(solution())