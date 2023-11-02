def solution():
    """Five hundred people attended the band concert. For that concert, the band gets 70% of the ticket price. If each ticket costs $30 and there are 4 members of the band, how much did each band member get from that concert?"""
    ticket_price = 30
    attendance = 500
    band_cut = 0.7
    total_revenue = ticket_price * attendance
    band_revenue = total_revenue * band_cut
    band_member_cut = band_revenue / 4
    result = band_member_cut
    return result

print(solution())