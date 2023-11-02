def solution():
    gold_coin_value = 50
    silver_coin_value = 25
    num_gold_coins = 3
    num_silver_coins = 5
    cash = 30
    
    # Calculate the total value of gold coins
    total_gold_value = num_gold_coins * gold_coin_value
    
    # Calculate the total value of silver coins
    total_silver_value = num_silver_coins * silver_coin_value
    
    # Calculate the total value of cash
    total_cash_value = cash
    
    # Calculate the total amount of money
    total_money = total_gold_value + total_silver_value + total_cash_value
    
    result = total_money
    return result

print(solution())