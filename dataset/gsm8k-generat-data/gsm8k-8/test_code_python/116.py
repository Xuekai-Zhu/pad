def solution():
    # Define the number of thank you cards
    thank_you_cards = 3

    # Define the number of bills
    bills = 2

    # Calculate the number of mail-in rebates
    rebates = bills + 3

    # Calculate the number of job applications
    job_applications = 2 * rebates

    # Calculate the total number of items to mail
    total_items = thank_you_cards + bills + rebates + job_applications

    # Calculate the number of stamps needed, accounting for the electric bill
    stamps_needed = total_items - 1 + 2

    result = stamps_needed
    return result

print(solution())