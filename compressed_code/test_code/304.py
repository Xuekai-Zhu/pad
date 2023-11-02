def solution():
    
    total_hours = 8
    customer_outreach_time = 4
    advertisement_time = customer_outreach_time / 2
    marketing_time = total_hours - customer_outreach_time - advertisement_time
    result = marketing_time
    return result

print(solution())