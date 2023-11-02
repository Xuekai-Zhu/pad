def solution():
    
    starting_bills = 10  
    percent_spent = 20
    remaining_bills = starting_bills - (starting_bills * (percent_spent / 100))
    exchange_rate = 1.5
    amount_received = remaining_bills * exchange_rate
    result = amount_received
    return result

print(solution())