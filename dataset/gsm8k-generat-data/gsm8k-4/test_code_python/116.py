def solution():
    """Valerie needs to put stamps on the envelopes she is about to mail. She has thank you cards for each of her grandmother, uncle and aunt for the birthday presents they sent. She also has to pay the water bill and the electric bill separately. She wants to send three more mail-in rebates than she does bills and she has twice as many job applications as rebates to mail. How many stamps does she need if everything needs 1 stamp except the electric bill, which needs 2?"""
    # Define the number of thank you cards
    num_thank_you_cards = 3

    # Define the number of bills and their total number of stamps needed
    num_bills = 2
    total_bill_stamps = num_bills * 1 + 2  # 2 stamps for the electric bill

    # Define the number of mail-in rebates and their total number of stamps needed
    num_rebates = num_bills + 3
    total_rebate_stamps = num_rebates * 1

    # Define the number of job applications and their total number of stamps needed
    num_job_apps = num_rebates * 2
    total_job_app_stamps = num_job_apps * 1

    # Calculate the total number of stamps needed
    total_stamps = num_thank_you_cards + total_bill_stamps + total_rebate_stamps + total_job_app_stamps

    # return the result
    result = total_stamps
    return result

print(solution())