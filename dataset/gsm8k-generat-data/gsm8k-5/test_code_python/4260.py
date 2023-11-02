def solution():
    bridgette_guests = 84  # Bridgette is inviting 84 guests
    alex_guests = bridgette_guests * (2/3)  # Alex is inviting two thirds of the number of guests Bridgette is inviting
    total_guests = bridgette_guests + alex_guests  # Total number of guests at the wedding
    extra_plates = 10  # The caterer will make 10 extra plates
    plates_needed = total_guests + extra_plates  # Total number of plates needed
    asparagus_per_plate = 8  # Each plate will have 8 asparagus spears

    # Calculate the total number of asparagus spears needed
    total_asparagus = plates_needed * asparagus_per_plate
    result = total_asparagus
    return result

print(solution())