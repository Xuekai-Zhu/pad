def solution():
    """Valerie needs to put stamps on the envelopes she is about to mail. She has thank you cards for each of her grandmother, uncle and aunt for the birthday presents they sent. She also has to pay the water bill and the electric bill separately. She wants to send three more mail-in rebates than she does bills and she has twice as many job applications as rebates to mail. How many stamps does she need if everything needs 1 stamp except the electric bill, which needs 2?"""
    thank_you_cards = 3
    bills = 2
    rebates = bills + 3
    job_applications = rebates * 2
    electric_bill = 2
    total_envelopes = thank_you_cards + bills + rebates + job_applications + electric_bill
    total_stamps = total_envelopes - electric_bill + 1
    result = total_stamps
    return result

print(solution())