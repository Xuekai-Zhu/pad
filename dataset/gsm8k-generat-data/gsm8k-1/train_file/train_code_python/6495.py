def solution():
    """The post office receives 60 letters and 20 packages per day. How many pieces of mail does it handle in six months if all the months have 30 days?"""
    letters_per_day = 60
    packages_per_day = 20
    days_in_six_months = 6 * 30
    total_mail = (letters_per_day + packages_per_day) * days_in_six_months
    result = total_mail
    return result

print(solution())