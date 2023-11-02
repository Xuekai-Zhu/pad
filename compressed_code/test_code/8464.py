def solution():
    
    initial_payment = 500
    couch_cost = 750
    table_cost = 100
    lamp_cost = 50
    total_cost = couch_cost + table_cost + lamp_cost
    remaining_balance = total_cost - initial_payment
    result = remaining_balance
    return result

print(solution())