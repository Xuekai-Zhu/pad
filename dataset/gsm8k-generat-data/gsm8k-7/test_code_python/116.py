def solution():
    num_thank_you_cards = 3
    num_bills = 2
    num_mail_in_rebates = num_bills + 3
    num_job_applications = num_mail_in_rebates * 2

    # Calculate the total number of items that need stamps
    total_items = num_thank_you_cards + num_bills + num_mail_in_rebates + num_job_applications
    
    # Calculate the total number of stamps needed
    total_stamps = (num_bills * 2) + total_items - num_bills
    result = total_stamps
    return result

print(solution())