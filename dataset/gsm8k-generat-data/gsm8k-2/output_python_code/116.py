def solution():
    """Valerie needs to put stamps on the envelopes she is about to mail. She has thank you cards for each of her grandmother, uncle and aunt for the birthday presents they sent. She also has to pay the water bill and the electric bill separately. She wants to send three more mail-in rebates than she does bills and she has twice as many job applications as rebates to mail. How many stamps does she need if everything needs 1 stamp except the electric bill, which needs 2?"""
    thank_you_cards = 3
    bills = 2
    mail_in_rebates = bills + 3
    job_applications = mail_in_rebates * 2
    total_envelopes = thank_you_cards + bills + mail_in_rebates + job_applications
    total_stamps = (thank_you_cards + bills + mail_in_rebates) + (2 * bills)
    result = total_stamps
    return result

print(solution())