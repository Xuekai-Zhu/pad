def solution():
    
    ticket_price = 30
    attendance = 500
    band_cut = 0.7
    total_revenue = ticket_price * attendance
    band_revenue = total_revenue * band_cut
    band_member_cut = band_revenue / 4
    result = band_member_cut
    return result

print(solution())