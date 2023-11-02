def solution():
    num_tickets = 25
    ticket_price = 2.0
    donation_1 = 15
    donation_2 = 15
    donation_3 = 20

    # Calculate the total amount raised from ticket sales
    ticket_sales = num_tickets * ticket_price

    # Calculate the total amount raised from donations
    donation_total = donation_1 + donation_2 + donation_3

    # Calculate the total amount raised
    total_amount_raised = ticket_sales + donation_total
    result = total_amount_raised
    return result

print(solution())