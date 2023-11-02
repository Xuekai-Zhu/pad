def solution():
    # Calculate the number of pieces of mail per day
    mail_per_day = 60 + 20
    # Calculate the number of pieces of mail in 6 months (assuming all months have 30 days)
    mail_in_6_months = mail_per_day * 30 * 6
    result = mail_in_6_months
    return result

print(solution())