def solution():
    
    num_rows = 5
    seats_per_row = 8
    seat_cost = 30
    total_seats = num_rows * seats_per_row
    subtotal = total_seats * seat_cost
    discount_groups = total_seats // 10
    discounted_seats = discount_groups * 10
    discounted_cost = subtotal / 10
    total_cost = subtotal - discounted_cost
    result = total_cost
    return result

print(solution())