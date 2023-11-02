def solution():
    initial_price = 100000  # Mr. Grey's house was worth $100,000
    profit_percent = 10  # Mr. Grey sold the house to Mr. Brown at a profit of 10%
    selling_price_1 = initial_price * (1 + (profit_percent/100))  # Mr. Brown's buying price

    loss_percent = 10  # Mr. Brown sold the house to his friend at a 10% loss
    selling_price_2 = selling_price_1 * (1 - (loss_percent/100))  # Mr. Brown's selling price
    
    result = selling_price_2
    return result

print(solution())