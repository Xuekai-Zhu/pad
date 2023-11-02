def solution():
    """John is budgeting for his marriage. The venue cost $10,000. It cost $500 for each guest, and John wants 50 guests while his wife wants 60% more than that. How much would the wedding cost if John's wife gets her way?"""
    venue_cost = 10000
    john_guests = 50
    wife_guests = int(john_guests * 1.6)
    guest_cost = 500
    total_guest_cost = (john_guests + wife_guests) * guest_cost
    total_cost = venue_cost + total_guest_cost
    result = total_cost
    return result

print(solution())