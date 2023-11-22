def solution():
    
    # Define the initial number of guests
    initial_guests = 100

    # Calculate the number of guests who elected an early checkout and a late checkout
    early_checkout_guests = 24
    late_checkout_guests = 15

    # Calculate the number of guests who checked in the afternoon
    afternoon_guests = 2 * late_checkout_guests

    # Calculate the total number of guests checked in
    total_guests = initial_guests + early_checkout_guests + late_checkout_guests + afternoon_guests - 7

    # return the result
    result = total_guests
    return result

print(solution())