def solution():
    """A business executive is going on a four day vacation where he will be unable to answer emails. The first day he is gone, he receives 16 new emails. On each of the following days, he receives half as many new emails as he received on the prior day. At the end of his four day vacation, how many new emails will he have received in total?"""
    total_emails = 0
    day1_emails = 16
    total_emails += day1_emails
    day2_emails = day1_emails / 2
    total_emails += day2_emails
    day3_emails = day2_emails / 2
    total_emails += day3_emails
    day4_emails = day3_emails / 2
    total_emails += day4_emails
    result = total_emails
    return result

print(solution())