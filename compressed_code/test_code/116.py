def solution():
    
    daniella_savings = 400
    ariella_savings = daniella_savings + 200
    interest_rate = 0.1
    ariella_interest = ariella_savings * interest_rate * 2
    total_ariella_savings = ariella_savings + ariella_interest
    result = total_ariella_savings
    return result

print(solution())