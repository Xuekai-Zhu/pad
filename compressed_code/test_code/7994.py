def solution():
    
    venue_cost = 10000
    john_guests = 50
    wife_additional_guests = john_guests * 0.6
    total_guests = john_guests + wife_additional_guests
    cost_per_guest = 500
    total_cost = venue_cost + (total_guests * cost_per_guest)
    result = total_cost
    return result

print(solution())