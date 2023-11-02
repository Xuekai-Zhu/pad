def solution():
    
    price_per_lawn = 33
    num_lawns = 16
    tip_per_customer = 10
    num_customers_tipped = 3
    total_price = price_per_lawn * num_lawns
    total_tips = tip_per_customer * num_customers_tipped
    money_made = total_price + total_tips
    result = money_made
    return result

print(solution())