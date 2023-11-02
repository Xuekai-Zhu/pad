def solution():
    thank_you_cards = 3  # Valerie has 3 thank you cards to mail
    bills = 2  # Valerie has 2 bills to mail (water and electric)
    mail_in_rebates = bills + 3  # Valerie needs to send 3 more rebates than bills
    job_applications = mail_in_rebates * 2  # Valerie has twice as many job applications as rebates to mail

    # Calculate the total number of stamps Valerie needs
    total_stamps = thank_you_cards + bills + mail_in_rebates + job_applications + 2  # Electric bill needs 2 stamps
    
    result = total_stamps
    return result

print(solution())