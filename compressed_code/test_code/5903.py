def solution():
    
    daniella_balance = 400
    ariella_balance = daniella_balance + 200
    interest_rate = 0.1
    years = 2
    ariella_interest = ariella_balance * interest_rate * years
    ariella_total = ariella_balance + ariella_interest
    result = ariella_total
    return result

print(solution())