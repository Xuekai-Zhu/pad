def solution():
    # Define the number of initial new emails
    day1_emails = 16

    # Calculate the number of new emails on each following day
    day2_emails = day1_emails / 2
    day3_emails = day2_emails / 2
    day4_emails = day3_emails / 2

    # Calculate the total new emails received during the four day vacation
    total_emails = day1_emails + day2_emails + day3_emails + day4_emails
    result = total_emails
    return result

print(solution())