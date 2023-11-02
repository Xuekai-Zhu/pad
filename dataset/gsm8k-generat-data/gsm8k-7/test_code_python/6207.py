def solution():
    treadmill_price = 1350
    discount = 0.3 # 30% discount
    plates_price = 50
    num_plates = 2

    # Calculate the discounted price of the treadmill
    discounted_treadmill_price = treadmill_price * (1 - discount)

    # Calculate the total cost of the plates
    total_plates_cost = plates_price * num_plates

    # Calculate the total cost of the treadmill and plates
    total_cost = discounted_treadmill_price + total_plates_cost
    result = total_cost
    return result

print(solution())