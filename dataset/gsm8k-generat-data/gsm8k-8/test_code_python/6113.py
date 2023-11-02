def solution():
    # Calculate the total number of seats needed for the 4-seater tables
    seats_4 = 6 * 4

    # Calculate the total number of seats needed for the 6-seater tables
    seats_6 = 12 * 6

    # Calculate the total number of chairs needed
    total_chairs = seats_4 + seats_6

    result = total_chairs
    return result

print(solution())