def solution():
    num_rows = 150
    num_seats_per_row = 10
    seat_price = 10.0
    empty_seats_percentage = 0.2

    # Calculate the total number of seats in the opera house
    total_seats = num_rows * num_seats_per_row

    # Calculate the number of seats that were not taken
    empty_seats = total_seats * empty_seats_percentage

    # Calculate the number of seats that were taken
    taken_seats = total_seats - empty_seats

    # Calculate the total earnings from the show
    total_earnings = taken_seats * seat_price
    result = total_earnings
    return result

print(solution())