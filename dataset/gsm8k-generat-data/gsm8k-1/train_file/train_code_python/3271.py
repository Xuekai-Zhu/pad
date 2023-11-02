def solution():
    """John has a very inefficient toilet that uses 5 gallons of water per flush and his household flushed 15 times per day. He replaced it with a toilet that uses 80% less water per flush. How much water did John save in June?"""
    inefficient_flush = 5
    efficient_flush = inefficient_flush * 0.2
    daily_savings = (inefficient_flush - efficient_flush) * 15
    days_in_june = 30
    total_savings = daily_savings * days_in_june
    result = total_savings
    return result

print(solution())