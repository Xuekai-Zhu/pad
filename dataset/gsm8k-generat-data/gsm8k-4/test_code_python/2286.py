def solution():
    """Marta works on her grandparent's farm to raise money for a new phone. So far, she has collected $240. For every hour she works, she receives $10. Her grandmother often gives her tips, and she has collected $50 in tips in total. How many hours has Marta worked on the farm so far?"""
    
    total_money = 240 + 50 # Add the tips to the total money collected
    
    hourly_pay = 10 # Marta earns $10 per hour
    
    hours_worked = total_money // hourly_pay # Divide the total money by the hourly pay to get the number of hours worked
    
    result = hours_worked
    return result

print(solution())