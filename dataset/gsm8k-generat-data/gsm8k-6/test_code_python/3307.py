def solution():
    # Find the amount of money Carla and Cosima have
    money_Natasha = 60
    money_Carla = money_Natasha / 3
    money_Cosima = money_Carla / 2
    
    # Find the total amount of money they have
    total_money = money_Natasha + money_Carla + money_Cosima
    
    # Find the buying price and selling price of the goods
    buying_price = total_money
    selling_price = (7/5) * buying_price
    
    # Calculate the profit they would make
    profit = selling_price - buying_price
    result = profit
    return result

print(solution())