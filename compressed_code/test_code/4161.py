def solution():
    
    days_in_month = 30
    regular_email_count = 20
    new_email_count = 25
    halfway_through_month = days_in_month // 2
    total_email_count = (regular_email_count * halfway_through_month) + (new_email_count * (days_in_month - halfway_through_month))
    result = total_email_count
    return result

print(solution())