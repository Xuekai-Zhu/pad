def solution():
    """The post office receives 60 letters and 20 packages per day. How many pieces of mail does it handle in six months if all the months have 30 days?"""
    letters_per_day = 60
    packages_per_day = 20
    total_mail_per_day = letters_per_day + packages_per_day
    days_per_month = 30
    total_mail_per_month = total_mail_per_day * days_per_month
    total_mail_six_months = total_mail_per_month * 6
    result = total_mail_six_months
    return result

print(solution())