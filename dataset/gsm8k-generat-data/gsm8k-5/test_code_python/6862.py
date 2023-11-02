def solution():
    total_attendees = 500  # 500 people attended the concert
    ticket_price = 30  # Each ticket costs $30
    band_percentage = 0.7  # The band gets 70% of the ticket price
    num_band_members = 4  # There are 4 members in the band

    # Calculate the total revenue from ticket sales
    total_revenue = total_attendees * ticket_price

    # Calculate the revenue earned by the band
    band_revenue = total_revenue * band_percentage

    # Calculate how much each band member gets
    amount_per_band_member = band_revenue / num_band_members
    result = amount_per_band_member
    return result

print(solution())