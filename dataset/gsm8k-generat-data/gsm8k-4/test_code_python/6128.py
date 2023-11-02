def solution():
    """An opera house has 150 rows; each row has ten seats. The ticket costs $10 per show. How much did the opera house earn from one of the shows if 20% of the seats were not taken?"""
    # Define the number of rows and seats per row
    rows = 150
    seats_per_row = 10

    # Calculate the total number of seats
    total_seats = rows * seats_per_row

    # Calculate the number of seats that were taken
    seats_taken = total_seats * 0.8

    # Calculate the total earnings from the show
    earnings = seats_taken * 10

    # return the result
    result = earnings
    return result

print(solution())