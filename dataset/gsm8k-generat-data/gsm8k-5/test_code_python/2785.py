def solution():
    venue_cost = 10000  # The venue cost is $10,000
    johns_guests = 50  # John wants 50 guests
    johns_guest_cost = 500  # Each guest costs $500

    # Calculate the total cost for John's guests
    johns_total_cost = johns_guests * johns_guest_cost

    # Calculate the number of guests that John's wife wants
    wife_guests = int(johns_guests * 1.6)

    # Calculate the total cost for John's wife's guests
    wife_total_cost = wife_guests * johns_guest_cost

    # Calculate the total cost for the wedding
    total_cost = venue_cost + johns_total_cost + wife_total_cost
    result = total_cost
    return result

print(solution())