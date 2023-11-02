def solution():
    
    price_per_head = 18
    num_customers = 80
    total_earnings = price_per_head * num_customers
    expenses = 280
    recreation_amount = 0.2 * total_earnings
    savings = total_earnings - (expenses + recreation_amount)
    result = savings
    return result

print(solution())