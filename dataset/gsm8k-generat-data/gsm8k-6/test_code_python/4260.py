def solution():
    # Calculate the total number of guests
    total_guests = 84 + (2/3) * 84  # Alex is inviting two thirds of the number of guests Bridgette is inviting
    total_guests += 10  # Caterer always makes 10 extra plates

    # Calculate the total number of asparagus spears needed
    asparagus_spears = total_guests * 8  # Each plate has 8 asparagus spears on it

    result = asparagus_spears
    return result

print(solution())