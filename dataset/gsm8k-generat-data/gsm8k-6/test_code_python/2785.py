def solution():
    # Calculate the cost of the venue and guests for John's wedding with 50 guests
    venue_cost = 10000  # cost of the venue
    guest_cost = 500 * 50  # cost of guests, $500 per guest for 50 guests
    total_cost = venue_cost + guest_cost  # total cost with 50 guests

    # Calculate the cost of guests if John's wife gets her way
    wife_guests = int(1.6 * 50)  # 60% more than 50 is 80, so total guests would be 50 + 80 = 130
    wife_guest_cost = 500 * wife_guests  # cost of guests for John's wife
    total_cost_wife = venue_cost + wife_guest_cost  # total cost with 130 guests

    result = total_cost_wife
    return result

print(solution())