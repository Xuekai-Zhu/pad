def solution():
    # Calculate the discounted price of the treadmill
    treadmill_price = 1350
    discount_percent = 30
    discount_amount = treadmill_price * (discount_percent / 100)
    discounted_treadmill_price = treadmill_price - discount_amount

    # Calculate the cost of two 45-pound plates
    plate_cost = 50
    total_plate_cost = plate_cost * 2

    # Calculate the total amount paid
    total_amount_paid = discounted_treadmill_price + total_plate_cost
    result = total_amount_paid
    return result

print(solution())