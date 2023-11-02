def solution():
    # Calculate the total revenue from ticket sales
    ticket_price = 30
    num_tickets_sold = 500
    total_revenue = ticket_price * num_tickets_sold

    # Calculate the revenue earned by the band
    band_share = 0.7
    band_revenue = band_share * total_revenue

    # Calculate the revenue earned by each band member
    num_band_members = 4
    revenue_per_band_member = band_revenue / num_band_members

    result = revenue_per_band_member
    return result

print(solution())