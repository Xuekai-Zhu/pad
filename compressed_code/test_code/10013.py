def solution():
    
    daily_emails = 20
    additional_emails = 5
    days_in_month = 30
    halfway_through = days_in_month // 2
    total_emails = (daily_emails * halfway_through) + ((daily_emails + additional_emails) * (days_in_month - halfway_through))
    result = total_emails
    return result

print(solution())