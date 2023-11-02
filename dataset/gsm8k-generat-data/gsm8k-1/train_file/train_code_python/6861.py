def solution():
    """Five hundred people attended the band concert. For that concert, the band gets 70% of the ticket price. If each ticket costs $30 and there are 4 members of the band, how much did each band member get from that concert?"""
    num_attendees = 500
    ticket_price = 30
    band_cut_percent = 0.7
    num_band_members = 4
    
    total_revenue = num_attendees * ticket_price
    band_cut = total_revenue * band_cut_percent
    band_member_cut = band_cut / num_band_members
    
    result = band_member_cut
    return result

print(solution())