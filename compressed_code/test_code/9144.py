def solution():
    
    bridgette_guests = 84
    alex_guests = bridgette_guests * (2/3)
    total_guests = bridgette_guests + alex_guests
    extra_plates = 10
    total_plates = total_guests + extra_plates
    asparagus_spears_per_plate = 8
    total_asparagus_spears = total_plates * asparagus_spears_per_plate
    result = total_asparagus_spears
    
    return result

print(solution())