def solution():
    
    inefficient_flush = 5
    efficient_flush = inefficient_flush * 0.2
    daily_savings = (inefficient_flush - efficient_flush) * 15
    days_in_june = 30
    total_savings = daily_savings * days_in_june
    result = total_savings
    return result

print(solution())