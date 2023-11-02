def solution():
    treadmill_price = 1350  # Original price of the treadmill
    discount = 0.3  # 30% discount on the treadmill
    plates_price = 50  # Price of each weight plate
    plates_quantity = 2  # Quantity of weight plates bought

    # Calculate the discounted price of the treadmill
    discounted_treadmill_price = treadmill_price - (treadmill_price * discount)

    # Calculate the total price of the weight plates
    plates_total_price = plates_price * plates_quantity

    # Calculate the total amount paid by Andre
    total_amount_paid = discounted_treadmill_price + plates_total_price
    result = total_amount_paid
    return result

print(solution())