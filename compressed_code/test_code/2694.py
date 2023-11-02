def solution():
    
    starting_bills = 10  
    spent_bills = int(starting_bills * 0.2)  
    remaining_bills = starting_bills - spent_bills
    exchange_rate = 1.5
    total_exchange = remaining_bills * exchange_rate
    result = total_exchange
    return result

print(solution())