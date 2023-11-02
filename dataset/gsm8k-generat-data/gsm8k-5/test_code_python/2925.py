def solution():
    number_of_rows = 40  # 40 rows of chairs were set up
    chairs_per_row = 20  # Each row had 20 chairs
    total_chairs = number_of_rows * chairs_per_row  # Calculate the total number of chairs

    unoccupied_seats = 10  # Only 10 seats were not occupied

    # Calculate the number of seats that were taken
    seats_taken = total_chairs - unoccupied_seats
    result = seats_taken
    return result

print(solution())