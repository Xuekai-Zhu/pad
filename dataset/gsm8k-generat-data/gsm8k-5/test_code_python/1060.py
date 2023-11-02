def solution():
    total_earrings = 12  # Barbie bought 12 pairs of earrings
    earrings_given = total_earrings / 2  # Barbie gave half of them to Alissa
    alissa_collections = earrings_given * 3 # Alissa's collections are triple the number of earrings she was given

    # Calculate the total number of earrings Alissa has now
    alissa_earrings = alissa_collections / 3

    result = alissa_earrings
    return result

print(solution())