def solution():
    """An opera house has 150 rows; each row has ten seats. The ticket costs $10 per show. How much did the opera house earn from one of the shows if 20% of the seats were not taken?"""
    # Define the number of rows and seats per row
    rows = 150
    seats_per_row = 10

    # Calculate the total number of seats
    total_seats = rows * seats_per_row

    # Calculate the number of seats not taken (20% of total seats)
    seats_not_taken = int(0.2 * total_seats)

    # Calculate the number of seats taken
    seats_taken = total_seats - seats_not_taken

    # Calculate the total earnings from the show
    total_earnings = seats_taken * 10

    # Display the total earnings
    result = total_earnings
    return result

print(solution())