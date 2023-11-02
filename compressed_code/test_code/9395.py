def solution():
    
    total_emails = 0
    day_emails = 16
    for i in range(4):
        total_emails += day_emails
        day_emails /= 2
    result = total_emails
    return result

print(solution())