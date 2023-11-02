def solution():
    
    initial_payment = 500
    couch_price = 750
    table_price = 100
    lamp_price = 50
    total_furniture_cost = couch_price + table_price + lamp_price
    remaining_balance = total_furniture_cost - initial_payment
    result = remaining_balance
    return result

print(solution())