def solution():
    """A local business was selling 25 raffle tickets to raise money for charity.  Each ticket cost $2.00 apiece.  They sold all the tickets and also received 2 $15 donations and a $20 donation.  How much money did they raise?"""
    # Define the cost of each raffle ticket
    TICKET_PRICE = 2.00

    # Define the number of raffle tickets sold
    tickets_sold = 25

    # Calculate the total money raised from raffle tickets
    raffle_money = TICKET_PRICE * tickets_sold

    # Calculate the total money raised from donations
    donation_money = (2 * 15) + 20

    # Calculate the total amount of money raised
    total_money = raffle_money + donation_money

    # Display the total amount of money raised
    result = total_money
    return result

print(solution())