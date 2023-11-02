def solution():
    """A business executive is going on a four day vacation where he will be unable to answer emails. The first day he is gone, he receives 16 new emails. On each of the following days, he receives half as many new emails as he received on the prior day. At the end of his four day vacation, how many new emails will he have received in total?"""
    # Define the number of new emails received on the first day
    first_day_emails = 16

    # Calculate the number of new emails received on the following days
    second_day_emails = first_day_emails / 2
    third_day_emails = second_day_emails / 2
    fourth_day_emails = third_day_emails / 2

    # Calculate the total number of new emails received during the vacation
    total_emails = first_day_emails + second_day_emails + third_day_emails + fourth_day_emails

    # Return the result
    result = total_emails
    return result

print(solution())