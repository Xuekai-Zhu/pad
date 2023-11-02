def solution():
    
    bridgette_guests = 84
    alex_guests = 2/3 * bridgette_guests
    total_guests = bridgette_guests + alex_guests
    extra_plates = 10
    total_plates = total_guests + extra_plates
    asparagus_per_plate = 8
    total_asparagus = total_plates * asparagus_per_plate
    result = total_asparagus
    return result

print(solution())