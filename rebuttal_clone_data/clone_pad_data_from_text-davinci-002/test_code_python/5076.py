def solution():
    TV_initial_price = 500
    TV_percent_increase = 2/5
    TV_increase_amount = TV_initial_price * TV_percent_increase
    TV_sale_price = TV_increase_amount + TV_initial_price
    
    phone_initial_price = 400
    phone_percent_increase = 40
    phone_increase_amount = phone_initial_price * (phone_percent_increase / 100)
    phone_sale_price = phone_increase_amount + phone_initial_price
    
    total_sale_price = TV_sale_price + phone_sale_price
    result = total_sale_price
    return result

print(solution())