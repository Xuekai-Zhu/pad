def solution():
    
    advertising_cost = 1000
    customers_brought = 100
    conversion_rate = 0.8
    purchase_amount = 25
    total_revenue = customers_brought * conversion_rate * purchase_amount
    profit = total_revenue - advertising_cost
    result = profit
    return result

print(solution())