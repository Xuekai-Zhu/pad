def solution():
    
    total_hours = 8
    customer_outreach_hours = 4
    advertisement_hours = customer_outreach_hours / 2
    marketing_hours = total_hours - customer_outreach_hours - advertisement_hours
    result = marketing_hours
    return result

print(solution())