def solution():
    rows_added = 5
    seats_per_row = 8
    seat_cost = 30
    total_seats = rows_added * seats_per_row
    discount_percent = 10
    discount_amount = total_seats * (discount_percent / 100)
    final_cost = (total_seats * seat_cost) - discount_amount
    result = final_cost
    return result

print(solution())