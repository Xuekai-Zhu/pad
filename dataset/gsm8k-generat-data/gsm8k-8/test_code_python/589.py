def solution():
    # Calculate the total number of pupils that can be seated at the rectangular tables
    total_rectangular_seats = 7 * 10

    # Calculate the remaining number of pupils that need to be seated
    remaining_pupils = 90 - total_rectangular_seats

    # Calculate the number of square tables needed to seat the remaining pupils
    square_tables_needed = remaining_pupils / 4

    # Round up to the nearest whole number
    square_tables_needed = math.ceil(square_tables_needed)

    result = square_tables_needed
    return result

print(solution())