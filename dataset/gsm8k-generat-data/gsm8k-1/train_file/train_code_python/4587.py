def solution():
    """A business executive is going on a four day vacation where he will be unable to answer emails. The first day he is gone, he receives 16 new emails. On each of the following days, he receives half as many new emails as he received on the prior day. At the end of his four day vacation, how many new emails will he have received in total?"""
    total_emails = 0
    day_emails = 16
    for i in range(4):
        total_emails += day_emails
        day_emails /= 2
    result = total_emails
    return result

print(solution())