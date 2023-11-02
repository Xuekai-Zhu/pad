def solution():
    """A local business was selling 25 raffle tickets to raise money for charity. Each ticket cost $2.00 apiece. They sold all the tickets and also received 2 $15 donations and a $20 donation. How much money did they raise?"""
    # Define the cost of each raffle ticket
    ticket_cost = 2

    # Calculate the total revenue from selling raffle tickets
    ticket_revenue = ticket_cost * 25

    # Calculate the total revenue from donations
    donation_revenue = 2 * 15 + 20

    # Calculate the total amount raised
    total_revenue = ticket_revenue + donation_revenue

    result = total_revenue
    return result

print(solution())