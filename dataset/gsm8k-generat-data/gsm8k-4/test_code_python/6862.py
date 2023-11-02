def solution():
    """Five hundred people attended the band concert. For that concert, the band gets 70% of the ticket price. If each ticket costs $30 and there are 4 members of the band, how much did each band member get from that concert?"""
    # Define the number of people who attended the concert and the price of each ticket
    num_attendees = 500
    ticket_price = 30

    # Calculate the total revenue from ticket sales
    total_revenue = num_attendees * ticket_price

    # Calculate the amount earned by the band
    band_earnings = total_revenue * 0.7

    # Calculate the earnings per band member
    band_member_earnings = band_earnings / 4

    # return the result
    result = band_member_earnings
    return result

print(solution())