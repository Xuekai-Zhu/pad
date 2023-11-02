def solution():
    total_hours = 8
    customer_outreach_hours = 4
    advertisement_hours = customer_outreach_hours / 2

    # Subtract the hours Bryan spends on customer outreach and advertisement from his total hours
    marketing_hours = total_hours - (customer_outreach_hours + advertisement_hours)
    result = marketing_hours
    return result

print(solution())