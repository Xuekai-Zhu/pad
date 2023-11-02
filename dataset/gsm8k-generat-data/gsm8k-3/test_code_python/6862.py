def solution():
    """Five hundred people attended the band concert. For that concert, the band gets 70% of the ticket price. If each ticket costs $30 and there are 4 members of the band, how much did each band member get from that concert?"""
    # Define the number of people who attended the concert and the ticket price
    ATTENDEES = 500
    TICKET_PRICE = 30

    # Calculate the total revenue from the concert
    total_revenue = ATTENDEES * TICKET_PRICE

    # Calculate the amount of revenue the band gets (70%)
    band_revenue = total_revenue * 0.7

    # Calculate the amount each band member gets
    member_share = band_revenue / 4

    # Display the amount each band member gets
    result = member_share
    return result

print(solution())