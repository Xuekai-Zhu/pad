def solution():
    num_emails = 16  # On the first day, the executive receives 16 new emails
    for day in range(2, 5):
        num_emails += num_emails / 2  # On each following day, the executive receives half as many new emails as the day before

    total_emails = num_emails * 4  # The executive was gone for four days, so multiply the number of emails by 4
    result = total_emails
    return result

print(solution())