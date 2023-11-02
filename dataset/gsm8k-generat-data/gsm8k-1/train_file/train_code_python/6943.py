def solution():
    """A local business was selling 25 raffle tickets to raise money for charity. Each ticket cost $2.00 apiece. They sold all the tickets and also received 2 $15 donations and a $20 donation. How much money did they raise?"""
    ticket_price = 2.0
    num_tickets = 25
    total_ticket_sales = ticket_price * num_tickets
    total_donations = 2 * 15 + 20
    total_raised = total_ticket_sales + total_donations
    result = total_raised
    return result

print(solution())