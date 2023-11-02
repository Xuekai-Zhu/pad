def solution():
    """John is budgeting for his marriage. The venue cost $10,000. It cost $500 for each guest, and John wants 50 guests while his wife wants 60% more than that. How much would the wedding cost if John's wife gets her way?"""
    venue_cost = 10000
    john_guests = 50
    wife_additional_guests = john_guests * 0.6
    total_guests = john_guests + wife_additional_guests
    cost_per_guest = 500
    total_cost = venue_cost + (total_guests * cost_per_guest)
    result = total_cost
    return result

print(solution())