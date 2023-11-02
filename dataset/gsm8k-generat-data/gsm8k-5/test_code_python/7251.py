def solution():
    coupe_price = 30000 # Melissa sells a coupe for $30,000
    suv_price = 2 * coupe_price # The SUV is sold for twice as much
    total_sales = coupe_price + suv_price # Calculate total sales
    commission_rate = 0.02 # Melissa's commission is 2%
    commission = commission_rate * total_sales # Calculate the commission earned
    result = commission
    return result

print(solution())