def solution():
    # Calculate the number of guests invited by Alex
    alex_guests = 84 * (2/3)

    # Calculate the total number of guests
    total_guests = 84 + alex_guests

    # Calculate the total number of plates needed
    total_plates = total_guests + 10

    # Calculate the total number of asparagus spears needed
    total_asparagus_spears = total_plates * 8

    result = total_asparagus_spears
    return result

print(solution())