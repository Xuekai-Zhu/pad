def solution():
    num_attendees = 500
    band_cut = 0.7
    ticket_price = 30
    num_band_members = 4

    # Calculate the total revenue from ticket sales
    total_revenue = num_attendees * ticket_price

    # Calculate the band's share of the revenue
    band_share = total_revenue * band_cut

    # Calculate the amount earned by each band member
    per_band_member_earnings = band_share / num_band_members
    result = per_band_member_earnings
    return result

print(solution())