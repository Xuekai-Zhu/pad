def solution():
    """Bridgette and Alex are getting married. Bridgette is inviting 84 guests, and Alex is inviting two thirds of that number of guests. They hired a caterer to make a plated meal for each guest at the wedding reception. The caterer always makes ten extra plates just in case something goes wrong. Each plate of steak and asparagus in garlic butter will have 8 asparagus spears on it. How many asparagus spears will the caterer need in all?"""
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