def solution():
    """Valerie needs to put stamps on the envelopes she is about to mail. She has thank you cards for each of her grandmother, uncle and aunt for the birthday presents they sent. She also has to pay the water bill and the electric bill separately. She wants to send three more mail-in rebates than she does bills and she has twice as many job applications as rebates to mail. How many stamps does she need if everything needs 1 stamp except the electric bill, which needs 2?"""
    # Define the number of thank you cards
    thank_you_cards = 3

    # Define the number of bills
    bills = 2

    # Calculate the number of mail-in rebates
    rebates = bills + 3

    # Calculate the number of job applications
    job_applications = rebates * 2

    # Calculate the total number of envelopes to mail
    envelopes = thank_you_cards + bills + rebates + job_applications

    # Calculate the number of stamps needed
    stamps = thank_you_cards + bills + rebates + (job_applications * 2) + 1  # electric bill needs 2 stamps

    result = stamps
    return result

print(solution())