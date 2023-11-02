def solution():
    venue_cost = 10000
    cost_per_guest = 500
    johns_guests = 50
    wife_guests = johns_guests * 1.6
    total_guests = johns_guests + wife_guests
    total_cost = venue_cost + (total_guests * cost_per_guest)
    result = total_cost
    return result

print(solution())