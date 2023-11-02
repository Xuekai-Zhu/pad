def solution():
    
    hotel_guests = 100
    early_checkout_guests = 24
    late_checkout_guests = 15
    afternoon_guests = 2 * early_checkout_guests
    after_dinner_guests = early_checkout_guests + late_checkout_guests + afternoon_guests
    total_guests = hotel_guests + after_dinner_guests
    result = total_guests
    return result

print(solution())